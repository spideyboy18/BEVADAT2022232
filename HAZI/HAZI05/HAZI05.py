import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import random
import math


class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float, random_seed: int):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.random_seed = random_seed

    def load_csv(self, csv_path: str) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
        random.seed(self.random_seed)
        df = pd.read_csv(csv_path, header=None)
        df = df.sample(frac=1, random_state=self.random_seed).reset_index(drop=True)
        x, y = df.iloc[:, :-1], df.iloc[:, -1]
        x = x.fillna(3.5)
        mask = (x <= 13.0) & (x >= 0.0)
        mask = mask.all(axis=1)
        x, y = x.loc[mask], y.loc[mask]
        x_train, y_train, x_test, y_test = self.train_test_split(x, y)
        return x_train, y_train, x_test, y_test

    def train_test_split(self, features: pd.DataFrame, labels: pd.Series) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        x_train, y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        x_test, y_test = features.iloc[train_size:train_size + test_size, :], labels.iloc[train_size:train_size + test_size]
        return x_train, y_train, x_test, y_test

    def euclidean(self, element_of_x: pd.Series) -> pd.Series:
        return ((self.x_train - element_of_x) ** 2).sum(axis=1).apply(lambda x: math.sqrt(x))

    def predict(self, x_test: pd.DataFrame) -> None:
        labels_pred = []
        for i in range(len(x_test)):
            distances = self.euclidean(x_test.iloc[i])
            distances = pd.concat([distances, self.y_train], axis=1)
            distances = distances.sort_values(0)
            label_pred = mode(distances.iloc[:self.k, 1], axis=0)[0][0]
            labels_pred.append(label_pred)
        self.y_preds = pd.Series(labels_pred)

    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def confusion_matrix(self) -> pd.DataFrame:
        return pd.DataFrame(confusion_matrix(self.y_test, self.y_preds), columns=self.y_test.unique(), index=self.y_test.unique())
    
    def best_k(self, x_test: pd.DataFrame, y_test: pd.DataFrame) -> Tuple[int, float]:
        best_k_val = 0
        best_accuracy = 0.0
        for k in range(1, 21):
            self.k = k
            self.predict(x_test)
            accuracy = self.accuracy()
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k_val = k
        return (best_k_val, round(best_accuracy, 2))

    @property
    def k_neighbors(self) -> int:
        return self.k
