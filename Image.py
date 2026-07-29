from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load the dataset
digits = load_digits()

# Features and labels
X = digits.data
y = digits.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = KNeighborsClassifier()
model.fit(X_train, y_train)

# Test the model
prediction = model.predict([X_test[0]])

# Display the image
plt.imshow(digits.images[len(X_train)], cmap="gray")
plt.title("Predicted Digit: " + str(prediction[0]))
plt.axis("off")
plt.show()

# Print actual and predicted values
print("Actual Digit   :", y_test[0])
print("Predicted Digit:", prediction[0])

# Display accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy * 100, 2), "%")