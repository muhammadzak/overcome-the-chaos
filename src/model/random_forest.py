from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import scikitplot.plotters as skplt
import matplotlib.pyplot as plt
import numpy as np
import pickle

from src.data.preprocess import read_preprocessed_data


class RandomForest(object):
    def __init__(self):
        self.clf = None

    def train(self, X, y):
        self.clf = RandomForestClassifier(n_estimators=50, max_depth=700)
        self.clf.fit(X, y)

    def plot_learning_curve(self, X, y):
        skplt.plot_learning_curve(self.clf, X, y)
        plt.show()

    def predict(self, dframe):
        X = dframe[['x0', 'x1', 'x2', 'x3']]
        y_pred = self.clf.predict(X)

        return y_pred

    def test_accuracy(self, dframe):
        X = dframe[['x0', 'x1', 'x2', 'x3']]
        y = dframe['y']
        y_pred = self.clf.predict(X)

        return accuracy_score(y, y_pred)

    def save(self, fname):
        with open(fname, 'wb') as ofile:
            pickle.dump(self.clf, ofile, pickle.HIGHEST_PROTOCOL)

    def load(self, fname):
        with open(fname, 'rb') as ifile:
            self.clf = pickle.load(ifile)


if __name__ == '__main__':
    c = RandomForest()
    data = read_preprocessed_data(r'c:\code\overcome-the-chaos\data\processed\preprocessed.pickle')
    c.train(data)
