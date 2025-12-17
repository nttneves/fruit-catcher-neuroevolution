import numpy as np

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []

        for i in range(len(layers) - 1):
            w = np.random.uniform(-1, 1, (layers[i] + 1, layers[i+1]))
            self.weights.append(w)

    def compute_num_weights(self):
        return sum(w.size for w in self.weights)

    def load_weights(self, flat):
        idx = 0
        for i in range(len(self.weights)):
            shape = self.weights[i].shape
            size = np.prod(shape)
            self.weights[i] = np.array(flat[idx:idx+size]).reshape(shape)
            idx += size

    def forward(self, x):
        a = np.array(x)
        for w in self.weights:
            a = np.append(a, 1)  # bias
            a = np.tanh(a @ w)
        return -1 if a[0] < 0 else 1


def create_network_architecture(state_size):
    # Perceptron:
    # return NeuralNetwork([state_size, 1])

    # Feedforward com hidden layer
    return NeuralNetwork([state_size, 8, 1])