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

A = np.array([[2, 5],
              [1, 2]], dtype=float)
a=np.array([21, 8])

B = np.array([[2, 3,-1],
              [3, 2,1],
              [1, -5,3]], dtype=float)
b=np.array([5, 10, 0])

LA, UA = doolittle_lu_decomposition(A)
LB, UB = doolittle_lu_decomposition(B)

ya = np.linalg.solve(LA, a)
res_a = np.linalg.solve(UA, ya)

yb = np.linalg.solve(LB, b)
res_b = np.linalg.solve(UB, yb)

print("Result 1:", res_a)
print("Result 2:", res_b)

