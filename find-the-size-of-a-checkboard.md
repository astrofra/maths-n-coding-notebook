# Find the size of each square of a checkboard

**How to find the size of each square of a checkboard in a jpeg image using openCV, using Python ?**

To define the size of each square of a checkerboard in a JPEG image using OpenCV and Python, you can follow these steps:

- First, you need to install OpenCV if you haven't already. You can install it using pip:

```bash
pip install opencv-python
```

- After installing OpenCV, you can use the following code to define the size of each square of a checkerboard in a JPEG image:

```python
import cv2
import numpy as np

def find_checkerboard_square_size(image_path, pattern_size):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Define the checkerboard pattern size (number of internal corners)
    # For example, for a 8x8 checkerboard, the pattern size should be (7, 7)
    pattern_size = pattern_size

    # Find the checkerboard corners
    found, corners = cv2.findChessboardCorners(image, pattern_size)

    if not found:
        print("Couldn't find the checkerboard pattern. Please check the input image and pattern size.")
        return None

    # Calculate the average square size
    square_sizes = []

    for i in range(pattern_size[1] - 1):
        for j in range(pattern_size[0] - 1):
            pt1 = corners[i * pattern_size[0] + j]
            pt2 = corners[i * pattern_size[0] + j + 1]
            pt3 = corners[(i + 1) * pattern_size[0] + j]

            square_size_x = np.linalg.norm(pt2 - pt1)
            square_size_y = np.linalg.norm(pt3 - pt1)
            quare_sizes.append((square_size_x, square_size_y))

    # Calculate the mean square size
    mean_square_size = np.mean(square_sizes, axis=0)
    return mean_square_size

if name == "main":
    # Specify the path to the input image
    image_path = "path/to/your/image.jpg"
    # Define the checkerboard pattern size (number of internal corners)
    pattern_size = (7, 7)

    square_size = find_checkerboard_square_size(image_path, pattern_size)

    if square_size is not None:
        print(f"Average size of each square: {square_size[0]:.2f} x {square_size[1]:.2f}")
```


This code will load the image, find the checkerboard corners using `cv2.findChessboardCorners`, and calculate the average size of each square. Make sure to adjust `image_path` and `pattern_size` to your specific case.

Keep in mind that the function `findChessboardCorners` works best with high-contrast images of checkerboards, where the checkerboard pattern is clearly visible.
