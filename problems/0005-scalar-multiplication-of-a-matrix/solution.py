import numpy as np
def scalar_multiply(a: list[list[int|float]], k: int|float) -> list[list[int|float]]:
    x = np.asarray(a)
    return k*x	