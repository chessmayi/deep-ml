# import numpy as np
# def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
# 	# Your code here, make sure to round
# 	m, n = X.shape
# 	w = np.zeros((n, 1))
# 	for i in range(iterations):
# 		w = w - alpha *1/m*X.T@(X@w - y)
# 	return w

import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    w = np.zeros((n, 1))
    
    # Ensure y is a column vector
    if y.ndim == 1:
        y = y.reshape(-1, 1)
    
    for i in range(iterations):
        gradient = (1/m) * X.T @ (X @ w - y)
        w = w - alpha * gradient
    
    # Round to 4 decimal places and flatten to 1D array
    return np.round(w, 4).flatten()