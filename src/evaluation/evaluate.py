from collections import namedtuple

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold
from tqdm import tqdm
import sys
import json
from pprint import pprint

sys.path.append('src')
import os
import pathlib

from models import RandomForestModel, SVMModel
from data import get_featues, get_label, read_processed_data

PROJ_DIR = str(pathlib.Path(__file__).parent.parent.parent)

preprocessed_data_fname = os.path.join(PROJ_DIR, 'data/processed/preprocessed.pickle')


def cv_evaluate_model(model, dframe):
    X = get_featues(dframe)
    y = get_label(dframe)
    kfold = StratifiedKFold(n_splits=10, shuffle=True)

    accuracy = np.empty(10)
    precision = np.empty(10)
    recall = np.empty(10)

    for i, (train_idx, test_idx) in tqdm(enumerate(kfold.split(X, y))):
        model.train(dframe.iloc[train_idx])
        predictions = model.predict(X.iloc[test_idx])

        accuracy[i] = accuracy_score(y[test_idx], predictions)
        precision[i] = precision_score(y[test_idx], predictions, average='macro')
        recall[i] = recall_score(y[test_idx], predictions, average='macro')

    results = {
        'params' : model.get_params(),
        'model' : model.name,
        'accuracy_std': np.std(accuracy),
        'accuracy_mean': np.mean(accuracy),
        'precision_std': np.std(precision),
        'precision_mean': np.mean(precision),
        'recall_std': np.std(recall),
        'recall_mean': np.mean(recall)
    }
    return results


def main():
    data = read_processed_data()

    classifiers = [RandomForestModel(), SVMModel()]
    for c in classifiers:
        pprint(cv_evaluate_model(c, data))



if __name__ == '__main__':
    main()
