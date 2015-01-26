from generator import *
from vec_and_matr import *
import numpy as np


def MPI(A, b, eps):
    h = []
    res = []
    delta = []
    vector = []
    n = len(A)
    
    tau = 2 / (1 + matrix_norm(A))
    for i in range(n):
        h.append(tau * b[i])

    new_A = multiply_by_number(A,tau)


    B = np.eye(n, n) - new_A
    steps = 0
    tmpx = h
    
    multiply = np.dot(B,tmpx)
    
    for i in range(n):
        res.append(h[i] + multiply[i])
    
    for i in range(n):
        delta.append(tmpx[i] - res[i])
    
    while np.linalg.norm(delta) > eps:
        steps += 1
        
        tmpx = vector_x_init(res)
        
        multiply = np.dot(B,tmpx)
        for i in range(n):
            res[i] = h[i] + multiply[i]
        for i in range(n):
            delta[i] = tmpx[i] - res[i]
        #print('res: ', res)  

     
    for i in range(n):
        vector.append(res[i] - tmpx[i])
    return res, steps, abs(np.linalg.norm(vector) / (1 - minnorm(A)))
