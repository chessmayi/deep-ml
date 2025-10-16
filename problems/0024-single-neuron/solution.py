import math
import numpy as np
def single_neuron_model(x: list[list[float]], y: list[int], w: list[float], b: float) -> (list[float], float):
	x = np.asarray(x)
	y = np.asarray(y)
	w = np.asarray(w)
	b = np.asarray(b)
	z  = x@w+b
	g = 1/(1+np.exp(-z))
	mse = np.mean((y-g)**2)
	return np.round(g,4).tolist(), mse
