import cv2
import numpy as np
import json

# Load images
img_orig = cv2.imread('optical-flow-deformation-calculation/img/standard.png', 0)
img_deform = cv2.imread('optical-flow-deformation-calculation/img/distorted.png', 0)

# Calculate optical flow
flow = cv2.calcOpticalFlowFarneback(img_orig, img_deform, None, 0.5, 3, 15, 3, 5, 1.2, 0)

# Optical flow returns a 2D array with (u,v) displacements for each pixel
# You can calculate the deformation magnitude for each pixel using the Euclidean norm
magnitude = np.sqrt(flow[...,0]**2 + flow[...,1]**2)

# Now, 'magnitude' is a 2D array of the same size as your images, 
# with the deformation rate for each pixel

# Calculate the max values before normalization
max_values = {
    'max_flow_x': float(np.max(flow[..., 0])),
    'max_flow_y': float(np.max(flow[..., 1])),
    'max_magnitude': float(np.max(magnitude))
}

# Save the max values to a JSON file
with open('optical-flow-deformation-calculation/max_values.json', 'w') as f:
    json.dump(max_values, f)

# Then proceed with the normalization and image saving

# Normalize the magnitude array to range 0-255
magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Save the normalized magnitude array as a bitmap image
cv2.imwrite('optical-flow-deformation-calculation/img/magnitude.png', magnitude_normalized)

# Normalize the flow components and magnitude to range 0-255
flow[..., 0] = cv2.normalize(flow[..., 0], None, 0, 255, cv2.NORM_MINMAX)
flow[..., 1] = cv2.normalize(flow[..., 1], None, 0, 255, cv2.NORM_MINMAX)
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

# Create a 3-channel RGB image using the flow components and magnitude
rgb = np.zeros((flow.shape[0], flow.shape[1], 3), dtype=np.uint8)
rgb[..., 0] = flow[..., 0]  # R channel
rgb[..., 1] = flow[..., 1]  # G channel
rgb[..., 2] = magnitude     # B channel

# Save the RGB image
cv2.imwrite('optical-flow-deformation-calculation/img/flow_direction_rgb.png', rgb)


