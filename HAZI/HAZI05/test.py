import pandas as pd
from HAZI05 import KNNClassifier
import os


kn = KNNClassifier(5, 0.1)

x,y = kn.load_csv('diabetes.csv')

kn.train_test_split(x,y)
kn.predict(kn.x_test)

kn.plot_confusion_matrix()

print(kn.accuracy())
print(kn.best_k())