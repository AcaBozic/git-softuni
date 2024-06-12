import numpy as np
import math as m

def dualobj(A):
    B = np.array([[0,-A[2,0],A[1,0]],[A[2,0],0,-A[0,0]],[-A[1,0],A[0,0],0]])
    return B

def unos_vektora():
    vektor = np.empty((3, 1), dtype=int)
    for i in range(3):
        vektor[i, 0] = int(input(f"Unesi {i+1} element vektora: "))
    return vektor



print("Unesi koordinate jedinicnog vektora e1: ")
e1 = unos_vektora()


print("Unesi koordinate jedinicnog vektora e2: ")
e2 = unos_vektora()

print("Unesi koordinate jedinicnog vektora e3: ")
e3 = unos_vektora()

q1 = float(input("Unesi vrednost ugla q1: "))
q2 = float(input("Unesi vrednost ugla q2: "))
q3 = float(input("Unesi vrednost ugla q3: "))

q1t = float(input("Unesi vrednost ugone brzine segmenta q1: "))
q2t = float(input("Unesi vrednost ugone brzine segmenta q2: "))
q3t = float(input("Unesi vrednost ugone brzine segmenta q3: "))


print("Unesi vrednost za vektor ro11: ")
ro11 = unos_vektora()

print("Unesi vrednost za vektor ro22: ")
ro22 = unos_vektora()

print("Unesi vrednost za vektor ro33: ")
ro33 = unos_vektora()

print("Unesi vrednost za vektor ro1: ")
ro1 = unos_vektora()

print("Unesi vrednost za vektor ro2: ")
ro2 = unos_vektora()

print("Unesi vrednost za vektor ro3: ")
ro3 = unos_vektora()


ksi1 = float(input("Uneti vrednost vektora ksi1: "))
ksi2 = float(input("Uneti vrednost vektora ksi2: "))
ksi3 = float(input("Uneti vrednost vektora ksi3: "))

I = np.identity(3, dtype=float)

# Rodrigova matrica transformacije za prvi segment je:

A01 = I +(1-ksi1)*((1-m.cos(q1))*(np.linalg.matrix_power(dualobj(e1),2))+m.sin(q1)*dualobj(e1))

# Rodrigova matrica transformacije za drugi segment u odnosu na prvi je:

A12 = I +(1-ksi2)*((1-m.cos(q2))*(np.linalg.matrix_power(dualobj(e2),2))+m.sin(q2)*dualobj(e2))

# Rodrigova matrica transformacije za treci segment u odnosu na drugi je:

A23 = I +(1-ksi3)*((1-m.cos(q3))*(np.linalg.matrix_power(dualobj(e3),2))+m.sin(q3)*dualobj(e3))

print("Rodrigova matrica transformacije za prvi segment je: ")
print(np.around(A01,4))
print()
print("Rodrigova matrica transformacije za drugi segment je: ")
print(np.around(A12,4))
print()
print("Rodrigova matrica transformacije za treci segment je: ")
print(np.around(A23,4))

A02 = A01.dot(A12)

A03 = A02.dot(A23)

A13 = A12.dot(A23)
print()
print("Matrica transformacije drugog segmenta u odnosu na nepokretnu tacku je: ")
print(np.around(A02,4))
print()
print("Matrica transformacije treceg segmenta u odnosu na nepokretnu tacku je: ")
print(np.around(A03,4))
print()
print("Matrica transformacije treceg segmenta u odnosu centar prvog segmenta je: ")
print(np.around(A13,4))
print("\n")

print("Polozaj centra inercije treceg segmenta je: \n")
rc3 = A01.dot(ro11) + A02.dot(ro22) + A03.dot(ro33) + A03.dot(ro3)
print(np.around(rc3,4))
print("\n")
print("Polozaj vrha hvataljke H je: \n")
rh0 = A01.dot(ro11) + A02.dot(ro22) + A03.dot(ro33)
print(np.around(rh0,4))

# odredjivanje vektora ugaone brzine treceg segmenta omega3

A31 = A13.transpose()

A32 = A23.transpose()

omega3 = q1t*A31.dot(e1) + q2t*A32.dot(e2) + q3t*I.dot(e3)
print()
print(f"Ugaona brzina treceg segmenta je: \n {np.around(omega3,4)} rad/s \n")

# Odredjivanje vektora brzine centra inercije prvog segmenta vi

vi = dualobj(e1).dot(ro11+ro1)*q1t
print(f"Brzina centra inercije prvog segmenta je: \n {np.around(vi,2)} m/s")
