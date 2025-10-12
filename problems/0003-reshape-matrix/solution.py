import numpy as np

def reshape_matrix(a: list[list[int|float]], k: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	x = np.asarray(a)
	x1, y1 = x.shape
	a,b = k
	if x1*y1 != a*b:
		return []
	return x.reshape(a,b).tolist()