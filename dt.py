import csv
import numpy as np
from collections import Counter

class DecisionTree:

    def __init__(self, X, y, threshold=1.0, max_depth=None): 
        # X é uma matriz de exemplos. EX: X = ['banana', 'yellow', 'curved'], ['apple', 'red', 'circle'], ... y é a lista com o resultado esperado. EX: y = [1, 1, ...]
        self.threshold = threshold
        self.max_depth = max_depth
        self.tree = self.build_tree(X, y, depth=0)

    def predict(self, x): 
        # (e.g. x = ['apple', 'green', 'circle'] -> 1 or -1)
        return self.predict_single(self.tree, x)
    
    def predict_single(self, node, x):
        if 'leaf' in node:
            return node['leaf']

        if x[node['split_attr']] == node['split_value']:
            return self.predict_single(node['left'], x)
        else:
            return self.predict_single(node['right'], x)

    def entropy(self, y):
        counter = Counter(y)
        total = len(y)
        entropy_value = 0
        for count in counter.values():
            p = count / total
            entropy_value += p * np.log2(p)
        return -entropy_value
        
    def information_gain(self, y, y_left, y_right):
        H_before = self.entropy(y)
        H_left = self.entropy(y_left)
        H_right = self.entropy(y_right)
        return H_before - (len(y_left)/len(y)) * H_left - (len(y_right)/len(y)) * H_right

    def best_split(self, X, y):
        best_gain = -1
        best_attr = None
        best_value = None
        best_sets = None

        num_features = len(X[0])

        for attr in range(num_features):
            values = set(example[attr] for example in X)
            for val in values:
                X_left, y_left, X_right, y_right = [], [], [], []

                for i in range(len(X)):
                    if X[i][attr] == val:
                        X_left.append(X[i])
                        y_left.append(y[i])
                    else:
                        X_right.append(X[i])
                        y_right.append(y[i])

                if len(X_left) == 0 or len(X_right) == 0:
                    continue

                gain = self.information_gain(y, y_left, y_right)
                if gain > best_gain:
                    best_gain = gain
                    best_attr = attr
                    best_value = val
                    best_sets = (X_left, y_left, X_right, y_right)

        return best_attr, best_value, best_sets

    def build_tree(self, X, y, depth):
        if len(set(y)) == 1:
            return {'leaf': y[0]}

        if self.max_depth is not None and depth >= self.max_depth:
            majority = Counter(y).most_common(1)[0][0]
            return {'leaf': majority}

        attr, val, sets = self.best_split(X, y)
        if attr is None or sets is None:
            majority = Counter(y).most_common(1)[0][0]
            return {'leaf': majority}

        X_left, y_left, X_right, y_right = sets

        return {
            'split_attr': attr,
            'split_value': val,
            'left': self.build_tree(X_left, y_left, depth + 1),
            'right': self.build_tree(X_right, y_right, depth + 1)
        }
    def train_decision_tree(X, y):
        # Replace with your configuration
        return DecisionTree(X, y)

