import numpy as np

def rnn_forward(x: list[list[float]], h: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	x = np.array(x)  # shape: (seq_len, input_size)
    h = np.array(h)  # shape: (hidden_size,)
    Wx = np.array(Wx)  # shape: (input_size, hidden_size)
    Wh = np.array(Wh)  # shape: (hidden_size, hidden_size)
    b = np.array(b)  # shape: (hidden_size,)

    for t in range(x.shape[0]):
        h = np.tanh(x[t] @ Wx.T + h @ Wh.T + b)
    return np.round(h, 4).tolist()