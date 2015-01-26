import random
import numpy as np

def matrix_generate(n):
    """Random generate, simmetric, diagonal dominance matrix"""
    a = np.eye(n)
    max = 0
    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(0,50)
            a[j][i] = a[i][j]
            if a[i][j] > max:
                max = a[i][j]
    for i in range(n):
        a[i][i] = max * n + random.randint(20,40)
    return np.array(a)


def vector_b_generate(n):
    """random generate"""
    return [random.randint(-60, 60) for element in range(n)]


def vector_init_0(n):
    """Initialization by zero"""
    return [ 0 for element in range (n)]


def vector_x_init(b):
    return [ element for element in b]
