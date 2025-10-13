import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	X = np.array(vectors)
    cov_matrix = np.cov(X, rowvar=True)
    return cov_matrix.tolist()