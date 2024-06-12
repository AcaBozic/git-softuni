import numpy as np

A = np.array([[0, 4, 12], [2, 4, -3], [-4, 0, -9]])
print("A = ", A)
print(A.ndim)
print(A.size)
print(A.shape)

B = np.empty([3,2], dtype = int)
print("B = ", B)

C = np.zeros((3, 4), dtype=int)
print("C= ", C)

D = np.ones((3, 3), dtype=float)
print("D = ", D)

E = np.full((3,2), 6)
print("E =", E)

I = np.identity(4, dtype=float)
print("I =",I)

import kreiranje_matrice
from kreiranje_matrice import A




print(A)


