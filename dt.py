import math
from collections import Counter, defaultdict

def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((c/total) * math.log2(c/total) for c in counts.values())

def information_gain(X, y, feature_index):
    base_entropy = entropy(y)
    subsets = defaultdict(list)

    for xi, label in zip(X, y):
        subsets[xi[feature_index]].append(label)

    weighted_entropy = 0
    for subset in subsets.values():
        weighted_entropy += (len(subset)/len(y)) * entropy(subset)

    return base_entropy - weighted_entropy


class DecisionTree:
    def __init__(self, X, y, features):
        self.label = None
        self.feature = None
        self.children = {}

        # Caso puro
        if len(set(y)) == 1:
            self.label = y[0]
            return

        # Sem atributos
        if not features:
            self.label = Counter(y).most_common(1)[0][0]
            return

        # Escolher melhor feature
        gains = [(information_gain(X, y, f), f) for f in features]
        _, best_feature = max(gains)
        self.feature = best_feature

        values = set(x[best_feature] for x in X)
        for v in values:
            sub_X, sub_y = [], []
            for xi, yi in zip(X, y):
                if xi[best_feature] == v:
                    sub_X.append(xi)
                    sub_y.append(yi)

            remaining_features = [f for f in features if f != best_feature]
            self.children[v] = DecisionTree(sub_X, sub_y, remaining_features)

    def predict(self, item):
        if self.label is not None:
            return self.label
        value = item[self.feature]
        if value not in self.children:
            return None
        return self.children[value].predict(item)


def train_decision_tree(X, y):
    features = list(range(len(X[0])))
    return DecisionTree(X, y, features)