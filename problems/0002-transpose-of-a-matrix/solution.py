import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    x = np.asarray(a)
	return x.T.tolist()