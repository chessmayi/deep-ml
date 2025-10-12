import numpy as np
def calculate_eigenvalues(a: list[list[float|int]]) -> list[float]:
	x = np.asarray(a)
	eig = np.linalg.eigvals(x)
    return eig.tolist()