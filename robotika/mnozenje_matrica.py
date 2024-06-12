import numpy as np
A = np.array( [[0,4,12],[2,4,-3],[4,0,-6]], dtype=int)
B = np.array( [[2,-4,2],[4,0,-6],[2,4,-3]], dtype = int)
E = np.array( [[1,0,0],[0,1,0],[0,0,1]])
print(A)
print()
print(B)
print()
print(E)
print()

D = A * B
print("D = ", D)


P = D/B
print("P = ", P)

E=A*A
print(E)

F = A**2

print(F)