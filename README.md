
```markdown
# Face Detection with OpenCV

This project demonstrates how to perform face detection on an image using OpenCV's Haar Cascade Classifier. The script loads an image, detects faces, and then highlights them with rectangles.

## Prerequisites

Before running the script, ensure you have the necessary libraries installed:

- Python 3.x
- OpenCV
- Matplotlib

You can install the required libraries using pip:

```bash
pip install opencv-python matplotlib
```

## How It Works

1. **Load Image**: The script starts by loading an image (`test image.jpg`) using OpenCV.
2. **Resize Image**: The image is resized to a fixed size (optional).
3. **Convert to Grayscale**: The loaded image is converted to grayscale to simplify the face detection process.
4. **Face Detection**: The Haar Cascade Classifier detects faces in the grayscale image.
5. **Draw Rectangles**: Rectangles are drawn around each detected face.
6. **Display Image**: The resulting image with highlighted faces is displayed using Matplotlib.

## Usage

1. Place your image file in the same directory as the script and name it `test image.jpg`. Alternatively, modify the script to use a different image file name.

2. Run the script:

```python
python face_detection.py
```

3. The script will display the image with rectangles around detected faces.

## Output

The script will display the image with detected faces highlighted by green rectangles. It will also print the number of faces detected.

## Example

An example of how the output might look:

![Example Output](example_output.png)

## Notes

- The `cv2.imshow` and `cv2.waitKey(0)` functions are not used in Jupyter Notebooks. Instead, the image is displayed using Matplotlib.
- Ensure the image path is correct and accessible.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

