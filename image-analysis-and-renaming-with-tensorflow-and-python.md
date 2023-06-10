# Image Analysis and Renaming with TensorFlow and Python

This repository contains a Python script that analyzes images from a given folder using TensorFlow and a pretrained model, and then renames each image file based on the identified content.

## Prerequisites

1. Python 3.7 or higher
2. TensorFlow 2.0 or higher

## Installation

1. Clone this repository on your local machine.
2. Install the necessary dependencies using pip:

```bash
pip install tensorflow
python image_renamer.py
```

This will go through all the images (.jpg, .png) in the specified folder, identify the content of each image using TensorFlow's pretrained ResNet50 model, and rename each image file with the identified content labels.

## Limitations

This script does not handle cases where two images end up with the same name after renaming. Also, if the TensorFlow model returns a large number of labels for an image, the filename could become very long. You might want to limit the number of keywords used for the filename, or use a different strategy to ensure filenames remain manageable.

```python
import os
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained model
model = ResNet50(weights='imagenet')

# Specify the folder to scan
folder_path = "/path/to/your/folder"

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        file_path = os.path.join(folder_path, filename)

        # Load the image
        img = image.load_img(file_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # Ask the model to identify the image
        preds = model.predict(x)
        labels = decode_predictions(preds, top=3)[0]  # We will get top 3 predictions

        # Extract the descriptions of these entities and sort them
        keywords = sorted([label[1].replace(" ", "_").lower() for label in labels])

        # Create the new filename from these keywords
        base, ext = os.path.splitext(filename)
        new_name = "_".join(keywords) + ext

        # Rename the file
        os.rename(file_path, os.path.join(folder_path, new_name))
```

