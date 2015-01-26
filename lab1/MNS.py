from generator import *
from vec_and_matr import *
import numpy as np


def MNS(A, b, eps):
    n = len(A)
    eigenvalue_min = min(np.linalg.eigvals(A))
    eigenvalue_max = max(np.linalg.eigvals(A))
    ro = (eigenvalue_max - eigenvalue_min) / (eigenvalue_max + eigenvalue_min)

    
    tmpx = b
    rk = []
    res = []
    vector = []
    delta = []
    x0 = tmpx
    steps = 0

    
    """Rk"""
    multiply = np.dot (A , tmpx)
    for i in range(n):
        rk.append(b[i] - multiply[i])

    """tk = np.vdot(rk, rk) / np.vdot(np.dot(A, rk), rk)"""    
    multiply_vec = np.vdot(rk, rk)
    multiply = np.dot(A, rk)
    multiply_vec2 = np.vdot(multiply, rk)
    tk = multiply_vec / multiply_vec2

    for i in range(n):
        res.append( rk[i] * tk + tmpx[i])

    for i in range(n):
        delta.append(tmpx[i] - res[i])

    while np.linalg.norm(delta) > eps:
        steps += 1

        tmpx = vector_x_init(res)
        

        """Rk"""
        multiply = np.dot (A , tmpx)
        for i in range(n):
            rk[i] = b[i] - multiply[i]        
        """Tk"""
        multiply_vec = np.vdot(rk, rk)
        multiply = np.dot(A, rk)
        multiply_vec2 = np.vdot(multiply, rk)
        tk = multiply_vec / multiply_vec2
        

        for i in range(n):
            res[i] = rk[i] * tk + tmpx[i]
        for i in range(n):
            delta[i] = tmpx[i] - res[i]
        #print('res: ', res)


    for i in range(n):
        vector.append(res[i] - x0[i])
    accuracy = abs(np.linalg.norm(vector) * pow(ro,steps))

    return res, steps, accuracy
