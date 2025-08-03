import numpy as np

def skew(vec: np.ndarray) -> np.ndarray:
    return np.array([[0., -vec[2], vec[1]],
                    [vec[2], 0., -vec[0]],
                    [-vec[1], vec[0], 0.]])

def rodrigues(axis_vec: np.ndarray, 
              angle: float) -> np.ndarray:
    skew = skew(axis_vec / np.linalg.norm(axis_vec))
    return np.eye(3) + np.sin(angle)*skew + (1-np.cos(angle))*(skew @ skew)