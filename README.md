# Image Classification Using Scikit-learn

## Project Description

This is a beginner-friendly machine learning project that performs image classification using Python and Scikit-learn. The project uses the built-in Digits dataset to classify handwritten digits (0-9) using a K-Nearest Neighbors (KNN) algorithm.

The model learns from training images and predicts the digit shown in a new image.

## Features

- Classifies handwritten digits from images
- Uses K-Nearest Neighbors (KNN) algorithm
- Displays the input image
- Shows predicted and actual values
- Calculates model accuracy

## Technologies Used

- Python
- Scikit-learn
- Matplotlib

## Project Files

```
Image-Classification/
│── image_classification.py
│── README.md
```

## Installation

Install the required libraries:

```bash
pip install scikit-learn matplotlib
```

## How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Run the Python file:

```bash
python image_classification.py
```

4. The program will display:
   - The input digit image
   - Predicted digit
   - Actual digit
   - Model accuracy

## Sample Output

```
Actual Digit   : 6
Predicted Digit: 6
Model Accuracy: 98.61 %
```

## How It Works

1. The Digits dataset is loaded from Scikit-learn.
2. The dataset is divided into training and testing data.
3. A K-Nearest Neighbors model is trained using training images.
4. The model predicts the digit from test images.
5. The accuracy of the model is calculated.

## Learning Outcomes

- Understanding image classification basics
- Working with machine learning models
- Using Scikit-learn datasets
- Training and testing ML models
- Making predictions from image data

## Future Improvements

- Add custom image upload feature
- Use Convolutional Neural Networks (CNN)
- Classify real-world images
- Create a web application using Flask or Streamlit

## Author

Your Name
