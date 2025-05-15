import csv
import numpy as np
from collections import Counter

class DecisionTree:

    def __init__(self, X, y, threshold=1.0, max_depth=None): # X é uma matriz de exemplos. EX: X = ['banana', 'yellow', 'curved'], ['apple', 'red', 'circle'], ... y é a lista com o resultado esperado. EX: y = [1, 1, ...]
        pass

    def predict(self, x): # (e.g. x = ['apple', 'green', 'circle'] -> 1 or -1)
        # Implement this
        pass

    def entropy(self, y):
        counter = Counter(y)
        total = len(y)
        entropy_value = 0
        for count in counter.values():
            p = count / total
            entropy_value += p * np.log2(p)
        return -entropy_value


def train_decision_tree(X, y):
    # Replace with your configuration
    return DecisionTree(X, y)
