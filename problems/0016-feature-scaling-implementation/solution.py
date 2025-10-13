import numpy as np
def feature_scaling(x: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	m = np.mean(x,axis=0)
    sd = np.std(x,axis=0)
    xx = x;
    xx = (xx - m)/sd
    min_val = np.min(x, axis=0)
    max_val = np.max(x, axis=0)
    normalized_data = (x - min_val) / (max_val - min_val)
    return xx,normalized_data