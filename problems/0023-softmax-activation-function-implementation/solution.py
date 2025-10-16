import math
import numpy as np
def softmax(a: list[float]) -> list[float]:
	a = np.asarray(a)
	res = np.exp(a)/np.sum(np.exp(a))
	return np.round(res,4).tolist()