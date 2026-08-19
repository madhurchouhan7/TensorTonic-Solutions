import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    matrix_transpose = np.swapaxes(A, 0,1)

    return matrix_transpose
