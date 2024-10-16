import numpy as np

def doolittle_lu_decomposition(A):
    n = len(A)
    L = np.eye(n)  
    U = np.zeros((n, n))  
    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    return L, U
def determinant_from_U(U):
    det = np.prod(np.diagonal(U))
    return det
def matrix_inverse(L, U):
    n = len(L)
    I = np.eye(n)  
    Y = np.zeros((n, n))
    for i in range(n):
        Y[i][i] = 1
        for j in range(i):
            Y[i] -= L[i][j] * Y[j]
    X = np.zeros((n, n))
    for i in range(n - 1, -1, -1):
        X[i] = Y[i]
        for j in range(i + 1, n):
            X[i] -= U[i][j] * X[j]
        X[i] /= U[i][i]

    return X
A = np.array([[2, 1,-1],
              [-3, -1,2],
              [-2, 1,2]], dtype=float)
B = np.array([[1, 1,1],
              [4, 3,-1],
              [-3, 5,3]], dtype=float)
LA, UA = doolittle_lu_decomposition(A)
LB, UB = doolittle_lu_decomposition(B)
detA=determinant_from_U(UA)
print('Determinent A: ' ,detA)
detB=determinant_from_U(UB)
print('Determinent B: ' ,detB)
inverseA=matrix_inverse(LA, UA)
print('Invere A: ')
print(inverseA)
inverseB=matrix_inverse(LB, UB)
print('Invere B: ')
print(inverseB)