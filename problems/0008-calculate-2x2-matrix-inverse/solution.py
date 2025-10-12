import numpy as np
def inverse_2x2(a: list[list[float]]) -> list[list[float]]:
    x = np.asarray(a)
    if np.linalg.det(x)==0:
        return None
    return np.linalg.inv(x).tolist()
	