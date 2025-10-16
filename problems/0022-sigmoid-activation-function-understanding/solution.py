import math
import numpy as np
def sigmoid(z: float) -> float:
	res = 1/(1+np.exp(-z))
	return np.round(res,4) 