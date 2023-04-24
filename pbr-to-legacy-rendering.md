# PBR textures into a legacy Phong rendering pipeline

**Let's say I have a GLSL shader that is written for a classic Phong/Lambert rendering pipeline.**

What if I want to interpret the values from a set of PBR textures (albedo, metalness, roughness) to control the diffuse color, specular intensity and specular glossiness and take advantage as much as possible of the PBR attributes ?
(yeah, legacy 3D software, you know...)

Well, to take advantage of PBR (Physically-Based Rendering) attributes using a classic Phong/Lambert shading model, you can interpret the PBR textures as follows:

- Albedo: Albedo represents the base color of a surface without reflections. In a Phong/Lambert shading model, you can use the albedo as the diffuse color. It can be directly sampled from the albedo texture.
- Metalness: Metalness represents whether a surface is metallic or not. In the Phong shading model, you can use this value to control the balance between diffuse and specular components. For metallic surfaces, the specular component will be more prominent, while for non-metallic surfaces, the diffuse component will be more prominent.
- Roughness: Roughness represents the microsurface details of a material. For the Phong shading model, you can use the roughness value to control the specular glossiness. A higher roughness value will result in a larger and more spread-out specular highlight, while a lower roughness value will result in a smaller and sharper specular highlight.

Here's an example of a GLSL shader that uses PBR textures with a Phong/Lambert shading model:

```glsl
// Vertex shader
#version 330 core

attribute vec3 aPosition;
attribute vec3 aNormal;
attribute vec2 aTexCoord;

varying vec3 vNormal;
varying vec2 vTexCoord;
varying vec3 vViewPos;

uniform mat4 uModelMatrix;
uniform mat4 uViewMatrix;
uniform mat4 uProjectionMatrix;
uniform mat3 uNormalMatrix;
uniform vec3 uCameraPosition;

void main() {
    vNormal = uNormalMatrix * aNormal;
    vTexCoord = aTexCoord;
    vec4 worldPos = uModelMatrix * vec4(aPosition, 1.0);
    vViewPos = uCameraPosition - worldPos.xyz;
    gl_Position = uProjectionMatrix * uViewMatrix * worldPos;
}

// Fragment shader
#version 330 core

varying vec3 vNormal;
varying vec2 vTexCoord;
varying vec3 vViewPos;

uniform sampler2D uAlbedoTexture;
uniform sampler2D uMetalnessTexture;
uniform sampler2D uRoughnessTexture;
uniform vec3 uLightPosition;
uniform vec3 uLightColor;

vec3 phongLambertShading(vec3 albedo, float metalness, float roughness, vec3 N, vec3 L, vec3 V) {
    vec3 H = normalize(L + V);

    // Diffuse component
    float NdotL = max(dot(N, L), 0.0);
    vec3 diffuse = albedo * (1.0 - metalness) * NdotL;

    // Specular component
    float NdotH = max(dot(N, H), 0.0);
    float specularIntensity = pow(NdotH, (1.0 - roughness) * 128.0);
    vec3 specular = (albedo * metalness + vec3(0.04 * (1.0 - metalness))) * specularIntensity;

    return diffuse + specular;
}

void main() {
    vec3 albedo = texture2D(uAlbedoTexture, vTexCoord).rgb;
    float metalness = texture2D(uMetalnessTexture, vTexCoord).r;
    float roughness = texture2D(uRoughnessTexture, vTexCoord).r;

    vec3 N = normalize(vNormal);
    vec3 L = normalize(uLightPosition - vViewPos);
    vec3 V = normalize(-vViewPos);

    vec3 color = phongLambertShading(albedo, metalness, roughness, N, L, V);

    // Apply the light color
    color *= uLightColor;

    // Gamma correction
    color = pow(color, vec3(1.0 / 2.2));

    gl_FragColor = vec4(color, 1.0);
}
```
