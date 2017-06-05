from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import scikitplot.plotters as skplt
from sklearn.multiclass import OneVsOneClassifier
import matplotlib.pyplot as plt
import numpy as np
import pickle

import sys

sys.path.append('src')

from data import get_featues, get_label


class SVMModel(object):
    def __init__(self):
        self.clf = OneVsOneClassifier(SVC())
        self.name = 'SVM'

    def get_params(self):
        return self.clf.get_params()

    def train(self, dframe):
        X = get_featues(dframe)
        y = get_label(dframe)
        self.clf.fit(X, y)

    def plot_learning_curve(self, dframe):
        X = get_featues(dframe)
        y = get_label(dframe)
        return skplt.plot_learning_curve(self.clf, X, y)

    def predict(self, X):
        y_pred = self.clf.predict(X)

        return y_pred

    def save(self, fname):
        with open(fname, 'wb') as ofile:
            pickle.dump(self.clf, ofile, pickle.HIGHEST_PROTOCOL)

    def load(self, fname):
        with open(fname, 'rb') as ifile:
            self.clf = pickle.load(ifile)
