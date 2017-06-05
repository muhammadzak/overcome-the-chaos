import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold

import sys
sys.path.append('src')
import os
import pathlib

from model.random_forest import RandomForest
from data.preprocess import read_preprocessed_data

PROJ_DIR = str(pathlib.Path(__file__).parent.parent.parent)

preprocessed_data_fname = os.path.join(PROJ_DIR, 'data/processed/preprocessed.pickle')


def cv_evaluate_model(clf, data):
    X = data[['x0', 'x1', 'x2', 'x3']]
    y = data['y']
    kfold = StratifiedKFold(n_splits=10, shuffle=True)
    for train_idx, test_idx in kfold.split(X, y):
        clf.train(X[train_idx], y[train_idx])
        predictions = clf.predict()


def main():
    data = read_preprocessed_data(preprocessed_data_fname)

    classifiers = [RandomForest()]
    for c in classifiers:
        cv_evaluate_model(c, data)

if __name__ == '__main__':
    main()