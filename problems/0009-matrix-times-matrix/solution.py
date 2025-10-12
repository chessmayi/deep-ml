import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	x = np.asarray(a)
    y = np.asarray(b)
    if x.shape[1]!=y.shape[0]:
        return -1
    return x@y.tolist()