import numpy as np

class NeuralNetwork:

    def __init__(self, input_size, hidden_architecture, hidden_activation, output_activation):
        self.input_size = input_size
        self.hidden_architecture = hidden_architecture
        self.hidden_activation = hidden_activation
        self.output_activation = output_activation
        self.hidden_weights = []
        self.hidden_biases = []
        self.output_weights = None
        self.output_bias = None

    def compute_num_weights(self):
        total_weights = 0
        input_size = self.input_size

        # Hidden layers
        for n_neurons in self.hidden_architecture:
            # Pesos + bias para cada neurónio
            total_weights += (input_size + 1) * n_neurons
            input_size = n_neurons

        # Output layer (1 neurónio)
        total_weights += input_size + 1

        return total_weights

    def load_weights(self, weights):
        w = np.array(weights)

        self.hidden_weights = []
        self.hidden_biases = []

        start_w = 0
        input_size = self.input_size
        for n in self.hidden_architecture:
            # biases
            self.hidden_biases.append(w[start_w:start_w + n])
            start_w += n
            # weights
            end_w = start_w + input_size * n
            self.hidden_weights.append(w[start_w:end_w].reshape(input_size, n))
            start_w = end_w
            input_size = n

        # output layer
        self.output_bias = w[start_w]
        start_w += 1
        self.output_weights = w[start_w:start_w + input_size]

    def forward(self, x):
        a = np.array(x)

        # Passagem pelas camadas escondidas
        for W, b in zip(self.hidden_weights, self.hidden_biases):
            a = self.hidden_activation(np.dot(a, W) + b)

        # Camada de saída
        output = np.dot(a, self.output_weights) + self.output_bias
        return self.output_activation(output)


def create_network_architecture(input_size):
    # ⬇️ Perceptron (sem camadas escondidas)
    # hidden_arch = ()

    # ⬇️ Feedforward com 1 camada escondida de 5 neurónios
    hidden_arch = (5,)

    hidden_fn = lambda x: 1 / (1 + np.exp(-x))  # Sigmóide
    output_fn = lambda x: 1 if x > 0 else -1    # Sinal

    return NeuralNetwork(input_size, hidden_arch, hidden_fn, output_fn)