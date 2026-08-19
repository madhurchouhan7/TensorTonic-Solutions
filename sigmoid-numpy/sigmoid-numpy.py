import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x=np.asarray(x)
    return np.where(
        x>=0,
        1 / (1 + np.exp(-x)), 
        np.exp(x) / (1 + np.exp(x))
    )
    