import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, epochs=1000, lr=0.0001, test_size=0.2, random_state=42):
        self.epochs = epochs
        self.lr = lr
        self.test_size = test_size
        self.random_state = random_state

    def load_data(self):
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)

        self.X = df['petal width (cm)'].values
        self.y = df['sepal length (cm)'].values

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=self.test_size, random_state=self.random_state)

    def fit(self):
        self.load_data()
        n = float(len(self.X_train))

        self.m = 0
        self.c = 0
        prev_loss = float('inf')
        delta = 1e-8
        self.losses = []

        for i in range(self.epochs):
            y_pred = self.m * self.X_train + self.c
            residuals = y_pred - self.y_train
            loss = np.sum(residuals ** 2)
            self.losses.append(loss)

            if abs(prev_loss - loss) < delta:
                break

            D_m = (-2/n) * np.sum(self.X_train * residuals)
            D_c = (-2/n) * np.sum(residuals)
            self.m -= self.lr * D_m
            self.c -= self.lr * D_c
            prev_loss = loss

    def predict(self, X):
        return self.m * X + self.c
