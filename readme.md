# Classical Computer Vision: Lane Line Extractor

## Overview
This project uses classical computer vision techniques with OpenCV to identify lane markings in static road images. It focuses on detecting white and yellow lane lines and reducing irrelevant parts of the image.

## Technologies Used
- Python
- OpenCV
- NumPy

## Image Processing Pipeline
The project processes road images through the following steps:

1. **Load Image:** Reads the input road image using OpenCV.
2. **HSV Color Filtering:** Converts the image from BGR to HSV color space and creates masks to identify white and yellow pixels.
3. **Grayscale Conversion:** Converts the filtered image to grayscale.
4. **Gaussian Blur:** Reduces noise and small details in the image.
5. **Canny Edge Detection:** Detects edges in the blurred image.
6. **Region of Interest (ROI):** Creates a polygon mask to focus on the road area.
7. **Final Lane Extraction:** Applies the ROI mask to the detected edges.

## Project Structure

lane-line-extractor/
├── images/
│   ├── image1.jpg
│   ├── image2.jpg
│   ├── image3.jpeg
│   └── image4.jpg
├── outputs
│   ├── image1
│   ├── image2
│   ├── image3
│   ├── image4
├── lane_detection.py
└── readme.md


## Requirements

Install Python, then install the required libraries:

```bash
pip install opencv-python numpy
```

## How to Run

1. Clone or download this repository.
2. Make sure the input road images are inside the `images` folder.
3. Open a terminal in the project folder.
4. Run:

```bash
python lane_detection.py
```

The script processes the images listed in the Python file and displays the processing stages. Output images are saved when the output paths and folders are available.

## Results

### Original Road Image
![Original Road Image](screenshots/original.jpg)

### White and Yellow Color Mask
![Color Mask](screenshots/color_mask.jpg)

### Gaussian Blur
![Gaussian Blur](screenshots/blurred.jpg)

### Canny Edge Detection
![Canny Edges](screenshots/edges.jpg)

### Final ROI-Masked Edges
![Final Lane Extraction](screenshots/final_lanes.jpg)

## Conclusion

This project demonstrates how classical computer vision techniques can be combined to isolate potential lane markings in road images. The results depend on image quality, lighting conditions, color thresholds, and the selected region of interest.
