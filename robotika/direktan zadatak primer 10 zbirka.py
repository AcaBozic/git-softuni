import numpy as np
import math as m

def unos_vektora():
    vektor = np.empty((3,1), dtype=float)
    for i in range (3) :
        vektor[i, 0] = float(input(f"Unesi {i+1} element vektora: "))
    return vektor

q1 = float(input("Unesi vrednost unutrasnje koordinate q1: "))
q2 = float(input("Unesi vrednost unutrasnje koordinate q2: "))
q3 = float(input("Unesi vrednost unutrasnje koordinate q3: "))

print("Unesi vrednost r11: ")
r11 = unos_vektora()

print("Unesi vrednost r22: ")
r22 = unos_vektora()

print("Unesi vrednost r33: ")
r33 = unos_vektora()

print("Unesi vrednost e1: ")
e1 = unos_vektora()

print("Unesi vrednost e2: ")
e2 = unos_vektora()

print("Unesi vrednost e3: ")
e3 = unos_vektora()

ksi1 = int(input("Unesi vrednost ksi1: "))
ksi2 = int(input("Unesi vrednost ksi2: "))
ksi3 = int(input("Unesi vrednost ksi3: "))

# matrice transformacije
A01 = np.array([[m.cos(q1), -m.sin(q1), 0],[m.sin(q1), m.cos(q1), 0],[0, 0, 1]])
A12 = np.array([[1, 0, 0] , [0, m.cos(q2), -m.sin(q2)] , [0, m.sin(q2), m.cos(q2)]])
A23 = np.identity(3,dtype = float)

A02 = A01.dot(A12)
A03 = A02.dot(A23)

# pozicija vrha hvataljke

rh = A01.dot(r11+ksi1*q1*e1) + A02.dot(r22+ksi2*q2*e2) + A03.dot(r33+ksi3*q3*e3)

print(f"Koordinata vrha hvataljke po x osi je: {rh[0][0]} m\n")
print(f"Koordinata vrha hvataljke po y osi je: {rh[1][0]} m\n")
print(f"Koordinata vrha hvataljke po z osi je: {rh[2][0]} m\n")
