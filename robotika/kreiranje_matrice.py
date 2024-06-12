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
         A[i][j] = float(input(f"A[ {i} ][ {j} ] = "))
 return A
def prikaz_rezultata(A):
    for red in A:
        for kolona in red:
            print(str(kolona), "\t", end = " ")
        print()
def main():
    m, n = unos_dimenzije_matrice()
    A = inicijalizacija_matrice(m, n)
    A = popunjavanje_matrice(m, n, A)

    prikaz_rezultata(A)
    return A

main()