import numpy as np
import math as m

alfa = float(input("Unesi ugao rotacije oko x ose: "))
beta = float(input("Unesi ugao rotacije oko y ose: "))
gama = float(input("Unesi ugao rotacije oko z ose: "))

# funkcija koja odredjuje dualni objekat vektora A
def dualobj(A):
    B = np.array([[0,-A[2,0],A[1,0]],[A[2,0],0,-A[0,0]],[-A[1,0],A[0,0],0]])
    return B

teta1 = np.array([[2*m.tan(m.radians(alfa/2))],[0], [0]])
teta2 = np.array([[0], [2*m.tan(m.radians(beta/2))], [0]])
teta3 = np.array([[0], [0], [2*m.tan(m.radians(gama/2))]])

# dualna matrica vektora konacne rotacije teta2
teta2d = np.array([[0, 0, 2*m.tan(m.radians(beta/2))],[0, 0, 0],[-2*m.tan(m.radians(beta/2)),0, 0]], dtype=float)

# dualna matrica vektora konacne rotacije teta3
teta3d = np.array([[0, -2*m.tan(m.radians(gama/2)), 0],[2*m.tan(m.radians(gama/2)), 0, 0],[0,0, 0]], dtype=float)

print(f"Dualna matrica vektora teta2 je: \n {teta2d}")
print("\n")

teta12=np.around(1/(1-1/4*teta1*teta2)*(teta1+teta2+1/2*(teta2d).dot(teta1)), 6)

# rezultat slaganja prve dve konacne rotacije je vektor konacne rotacije za ove dve rotacije
print(teta12)

# rezultujuca konacna rotacija nakon sve tri rotacije je
# teta=1/(1-1/4*teta12*teta3)*(teta12+teta3+1/2*(teta3d).dot(teta12))

# teta = 1/(1-1/4*teta12*teta3)*(teta12+teta3+1/2*dualobj(teta3).dot(teta12))

teta = np.array([[0.0541367],[1.06931],[0.876555]])

print(f"Rezultujuca konacna rotacija dobijena rotacijom oko sve tri ose je:\n{teta}")

# intenzitet vektora konacne rotacije teta je
teta_intenz = np.linalg.norm(teta)
print(f"\n Inenzitet vektora konacne rotacije teta je: {teta_intenz}\n")

# jedinacni vektor konacne rotacije je
e = teta/teta_intenz
print(f"jedinacni vektor konacne rotacije teta je e: \n {e}\n")

# ugao fi konacne rotacije je
fi = m.degrees(2* m.atan(teta_intenz/2))
print(f"ugao konacne rotacije je: {fi}\n")



I = np.identity(3, dtype=float)


A = (1/2*dualobj(teta)+I)*np.linalg.inv(1/2*dualobj(teta)-I)


print(f"Matrica transformacije je: \n{A}\n")

# alternativni nacini pronalaska matrice transformacije
# A1 = I + 4/(4+teta**2)*(1/2*(dualobj(teta)).dot(dualobj(teta)) + dualobj(teta))
#
# print(A1)
# print("\n")
#
# A2 = I +(1-np.cos(fi))*(np.linalg.matrix_power(dualobj(e),2)) + np.sin(fi)*dualobj(e)
#
# print(A2)
#

# kvadriranje dualnog objekta matrice B
# B = np.array([[1],[2],[3]])

# 1. nacin
# e=dualobj(B).dot(dualobj(B))
# print(e)

# 2. nacin pomocu funkcije matrix_pover i stepena 2
# m = np.linalg.matrix_power(dualobj(B),2)
# print(m)


# hamilton - rodrigovi parametri
lamda0 = np.sqrt(1/(1+1/4*(teta_intenz)**2))
print(lamda0)

lamda1 = teta1/2*lamda0
print(lamda1)

lamda2 = teta2/2*lamda0
print(lamda2)

lamda3 = teta3/2*lamda0
print(lamda1)








