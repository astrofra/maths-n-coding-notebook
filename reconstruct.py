import json
import cv2
import numpy as np

# Load the deformed image
img_deform = cv2.imread('optical-flow-deformation-calculation/img/distorted.png', 0)

# Load the RGB flow image
flow_bgr = cv2.imread('optical-flow-deformation-calculation/img/flow_direction_rgb.png')

# Load the max values from the JSON file
with open('optical-flow-deformation-calculation/max_values.json', 'r') as f:
    max_values = json.load(f)

# Convert the BGR flow image back to the original flow values
flow = np.zeros((flow_bgr.shape[0], flow_bgr.shape[1], 2), dtype=np.float32)
flow[..., 0] = flow_bgr[..., 1] * max_values['max_flow_x'] / 255  # G channel
flow[..., 1] = flow_bgr[..., 2] * max_values['max_flow_y'] / 255  # R channel

# # Convert the RGB flow image back to the original flow values
# flow = np.zeros((flow_rgb.shape[0], flow_rgb.shape[1], 2), dtype=np.float32)
# flow[..., 0] = flow_rgb[..., 0] * max_values['max_flow_x'] / 255
# flow[..., 1] = flow_rgb[..., 1] * max_values['max_flow_y'] / 255

# Create a grid of pixel coordinates in the deformed image
y_coords, x_coords = np.mgrid[0:img_deform.shape[0], 0:img_deform.shape[1]]

# Subtract the flow from the coordinates to get the coordinates in the original image
map_y, map_x = (y_coords - flow[..., 1]).astype('float32'), (x_coords - flow[..., 0]).astype('float32')

# Use remap to warp the deformed image back to the original image
reconstructed = cv2.remap(img_deform, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

# Save the reconstructed image
cv2.imwrite('optical-flow-deformation-calculation/img/reconstructed.png', reconstructed)
