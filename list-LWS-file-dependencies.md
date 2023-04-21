# List the dependencies of a .LWS file

**Explore the depencies of the .LWS scene format from Lightwave 3D software and store all the listed .LWO in a dictionnary**

This Python script that can parse an .LWS scene file and extract all .LWO file paths, then store them in a dictionary. This code assumes that you have a valid .LWS scene file, and it only searches for .LWO file paths that are listed in the 'LoadObjectLayer' lines.

```python
import re

def parse_lws_file(file_path):
    lwo_files = {}
    object_index = 1

    with open(file_path, 'r') as lws_file:
        for line in lws_file:
            if line.startswith("LoadObjectLayer"):
                lwo_path = re.search(r'"(.*\.lwo)"', line)
                if lwo_path:
                    lwo_file = lwo_path.group(1)
                    lwo_files[f'Object{object_index}'] = lwo_file
                    object_index += 1

    return lwo_files

if __name__ == "__main__":
    lws_file_path = "path/to/your/scene.lws"
    lwo_files_dict = parse_lws_file(lws_file_path)
    print("LWO files found in the LWS scene:")
    for key, value in lwo_files_dict.items():
        print(f"{key}: {value}")
```
