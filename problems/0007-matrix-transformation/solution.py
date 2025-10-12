import numpy as np
def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    a = np.asarray(A)
    t = np.asarray(T)
    s = np.asarray(S)
    if np.linalg.det(t)==0 or np.linalg.det(s)==0:
        return -1
    return np.linalg.inv(t)@a@s.tolist()