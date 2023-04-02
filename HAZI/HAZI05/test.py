import pandas as pd
from HAZI05 import KNNClassifier

# Load data from a CSV file using Pandas


# Create an instance of the KNNClassifier class
knn = KNNClassifier(k=3, test_split_ratio=0.2, random_seed=42)
knn.load_csv("data/iris.csv")
# Split the data into training and testing sets

# Train the classifier

# Test the classifier

# Print the accuracy and confusion matrix
print("Accuracy:", knn.accuracy())
print("Confusion matrix:\n", knn.confusion_matrix())