import numpy as np
def calculate_matrix_mean(a: list[list[float]], mode: str) -> list[float]:
	x = np.asarray(a)
	if mode == 'column':
		return x.mean(axis=0)
	return x.mean(axis=1)