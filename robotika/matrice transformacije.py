import numpy as np

def unos_dimenzije_matrice():
 x = int(input("Uneti broj redova matrice: "))
 y = int(input("Uneti broj kolona matrice: "))
 return x, y
def inicijalizacija_matrice(x, y):
 A = [[0 for j in range(y)] for i in range(x)]
 return A
def popunjavanje_matrice(x, y, A):
 for i in range(x):
     for j in range(y):
         A[i][j] = float(input("A[" + str(i) + "][" + str(j) + "] = "))
 return A


def main():
    m, n = unos_dimenzije_matrice()
    A = inicijalizacija_matrice(m, n)
    A = popunjavanje_matrice(m, n, A)
    I = np.identity(3, dtype=float)
    Qd = 2*(A-I).dot(np.linalg.inv(A+I))
    Qd = np.around(Qd,4)
    print("Vektor konacne rotacije je:")
    print(Qd)


main()



