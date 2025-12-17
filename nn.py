# nn.py
import numpy as np

class SimpleRNN:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size

        self.Wx = np.random.uniform(-1, 1, (hidden_size, input_size))
        self.Wh = np.random.uniform(-1, 1, (hidden_size, hidden_size))
        self.bh = np.random.uniform(-1, 1, hidden_size)

        self.Wy = np.random.uniform(-1, 1, hidden_size)
        self.by = np.random.uniform(-1, 1)

        self.reset_state()

    def reset_state(self):
        self.h = np.zeros(self.hidden_size)

    def compute_num_weights(self):
        return (
            self.Wx.size +
            self.Wh.size +
            self.bh.size +
            self.Wy.size +
            1
        )

    def load_weights(self, flat):
        flat = np.array(flat)
        idx = 0

        def take(n):
            nonlocal idx
            chunk = flat[idx:idx+n]
            idx += n
            return chunk

        self.Wx = take(self.Wx.size).reshape(self.Wx.shape)
        self.Wh = take(self.Wh.size).reshape(self.Wh.shape)
        self.bh = take(self.bh.size)

        self.Wy = take(self.Wy.size)
        self.by = take(1)[0]

    def forward(self, x):
        x = np.array(x)

        self.h = np.tanh(
            self.Wx @ x +
            self.Wh @ self.h +
            self.bh
        )

        return self.Wy @ self.h + self.by


def create_network_architecture(state_size):
    return SimpleRNN(input_size=state_size, hidden_size=6)