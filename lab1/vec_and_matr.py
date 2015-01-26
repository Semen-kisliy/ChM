from math import *
import numpy as np


def vector_multiply(b, number):
    for i in range(len(b)):
        b[i] *= number
    return b


def multiply_by_number(A, number):
    """For matrix"""
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= number
    return A


def trance(A):
    T = list(zip(*A))
    return T


def matrix_vector_multiply(A,b):
    answer = []
    if len(A[0]) != len(b):
        print ('Amount of columns in first matrix not equal to amount of elements in vector')
    else:
        sum = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                sum += A[i][j]*b[j]
            answer.append(sum)
    return answer


def matrix_norm(A):
    """summ of all elements in matrix"""
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            sum += abs(A[i][j])
    return sum


def matrix_norm2(A):
    """max summ of elements in line"""
    norm = []
    element = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            element += abs(A[i][j])
        norm.append(element)
    return max(norm)


def matrix_norm3(A):
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            sum += pow(A[i][j], 2)
    return pow( sum, 0.5 )


def minnorm(A):
    AT = trance(A)
    return min([matrix_norm(A), matrix_norm2(A),matrix_norm3(A),matrix_norm3(AT)])


def print_matrix(matrix):
    for row in matrix:
        print (row)
        

def check_square(matrix):
    return len(matrix) == len(matrix[0])

def check_simmetric(matrix):
    ok = True
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                ok = False
    return ok

def check_positive(matrix):
    of = True
    eigenvalue = np.linalg.eigvals(matrix)
    for i in eigenvalue:
        if i < 0:
            ok = False
    return ok


def minor(matrix, i, j):
    """ Возвращает дополнительный минор к элементу i, j доп. к функции determinant"""
 
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp
    # return list(zip(*tmp))
    

def determinant(matrix):
    """ Определитель квадратной матрицы """
    size = len(matrix)
    if size == 2:
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
 
    return sum((-1)**j * matrix[0][j] * determinant(minor(matrix, 0, j))
            for j in range(size))
