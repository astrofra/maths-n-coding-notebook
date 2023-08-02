# Optical Flow Deformation Calculation with OpenCV in Python

This repository provides a Python script to calculate the deformation rate per pixel between an original image and a deformed image using optical flow. The script uses the OpenCV library to calculate the optical flow using the Farnebäck method.

## Dependencies

- Python 3.6 or later
- OpenCV
- NumPy

You can install the dependencies with pip:

```bash
pip install opencv-python numpy
```

## Usage

```python
import cv2
import numpy as np

# Load images
img_orig = cv2.imread('original.png', 0)
img_deform = cv2.imread('deformed.png', 0)

# Calculate optical flow
flow = cv2.calcOpticalFlowFarneback(img_orig, img_deform, None, 0.5, 3, 15, 3, 5, 1.2, 0)

# Optical flow returns a 2D array with (u,v) displacements for each pixel
# You can calculate the deformation magnitude for each pixel using the Euclidean norm
magnitude = np.sqrt(flow[...,0]**2 + flow[...,1]**2)

# Now, 'magnitude' is a 2D array of the same size as your images, 
# with the deformation rate for each pixel
```

### Explanation of cv2.calcOpticalFlowFarneback parameters

- **prev:** Input previous (or reference) grayscale image.
- **next:** Input next (or target) grayscale image.
- **flow:** Initial optical flow estimate. If you don't have it, you can leave it as None.
- **pyr_scale:** Scale between pyramid levels. 0.5 means a classical pyramid, where each next layer is twice smaller than the previous one.
- **levels:** Number of pyramid levels, including the initial image. Pyramid levels allow the algorithm to work at different resolutions.
- **winsize:** Averaging window size, usually 15. The larger the size, the more the algorithm can consider large displacements.
- **iterations:** Number of iterations at each pyramid level.
- **poly_n:** Size of the pixel neighborhood used to find polynomial expansion in each pixel; typically poly_n =5 or 7.
- **poly_sigma:** Standard deviation of the Gaussian that is used to smooth derivatives used as a basis for the optical flow. It can affect the final result as it affects the window size of the polynomial filter.
- **flags:** Additional option that can be 0 or a combination of cv2.OPTFLOW_USE_INITIAL_FLOW and cv2.OPTFLOW_FARNEBACK_GAUSSIAN.

These parameters allow you to control the accuracy and window size of the algorithm, which can impact the quality of the calculated optical flow.

## Store the optical flow map

To store the content of the magnitude array into a bitmap image, you can use the imwrite function from OpenCV. However, before saving the image, you should normalize the magnitude array to the range 0-255, as pixel intensities in an image are usually 8-bit, ranging from 0 (black) to 255 (white).

```python
# Normalize the magnitude array to range 0-255
magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Save the normalized magnitude array as a bitmap image
cv2.imwrite('magnitude.bmp', magnitude_normalized)
```

In this code, cv2.normalize is used to normalize the magnitude array to the range 0-255. The astype(np.uint8) function is used to convert the normalized array to 8-bit unsigned integers, which is the standard format for pixel intensities in an image.

Then, cv2.imwrite is used to save the normalized magnitude array as a bitmap image. The resulting image will be a grayscale image where the intensity of each pixel corresponds to the deformation rate at that pixel in the original images.

