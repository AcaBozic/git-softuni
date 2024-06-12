from typing import Any

import numpy as np
import math as m

from numpy import ndarray, dtype


def unos_vektora():
    vektor = np.empty((3, 1), dtype=float)
    for i in range(3):
        vektor[i, 0] = float(input(f"Unesi {i+1} element vektora: "))
    return vektor

q1 = float(input("Unesi vrednost ugla rotacije prvog segmenta q1: "))
q2 = float(input("Unesi vrednost ugla rotacije drugog segmenta q2: "))
q3 = float(input("Unesi vrednost ugla rotacije treceg segmenta q3: "))

print("Unesi vrednost za vektor r11: ")
r11 = unos_vektora()

print("Unesi vrednost za vektor r22: ")
r22 = unos_vektora()

print("Unesi vrednost za vektor r33: ")
r33 = unos_vektora()

# matrica transformacije prvog segmenta u odnosu na fiksnu tacku koordinatnog pocetka
A01 = np.array([[1, 0, 0],[0, m.cos(q1), -m.sin(q1)], [0, m.sin(q1), m.cos(q1)]])
print(A01)
print()

#  matrica transformacije drugog segmenta u odnosu na prvi
A12 = np.array([[m.cos(q2), 0, m.sin(q2)] , [0, 1, 0] , [-m.sin(q2), 0, m.cos(q2)]])
print(A12)
print()

#  matrica transformacije treceg segmenta u odnosu na drugi
A23 = np.array([[1, 0, 0] , [0, m.cos(q3), -m.sin(q3)] , [0, m.sin(q3), m.cos(q3)]])
print(A23)
print()

#  matrica transformacije drugog segmenta u odnosu na fiksnu tacku koordinatnog pocetka
A02 = A01.dot(A12)

#  matrica transformacije treceg segmenta u odnosu na fiksnu tacku koordinatnog pocetka
A03 = A02.dot(A23)

print("matrica trasformacije A01 je:\n")
print(np.around(A01, 3))
print()
print("matrica trasformacije A02 je:\n")
print(np.around(A02, 3 ))
print()
print("matrica trasformacije A03 je:\n")
print(np.around(A03, 3))
print()

# pozicija vrha hvataljke
print("pozicija vrha hvataljke je: \n")
rh = A01.dot(r11) + A02.dot(r22) + A03.dot(r33)
print(rh)

# prvi redovi matrica transformacije A01, A02, A03
A011 = np.array([A01[0][0],A01[0][1],A01[0][2]])
A021 = np.array([A02[0][0],A02[0][1],A02[0][2]])
A031 = np.array([A03[0][0],A03[0][1],A03[0][2]])

# pozicija po x vrha hvataljke
xh = A011.dot(r11) + A021.dot(r22) + A031.dot(r33)
print(f"xh je {xh}")

# drugi redovi matrica transformacije A01, A02, A03
A012 = np.array([A01[1][0],A01[1][1],A01[1][2]])
A022 = np.array([A02[1][0],A02[1][1],A02[1][2]])
A032 = np.array([A03[1][0],A03[1][1],A03[1][2]])
yh = A012.dot(r11) + A022.dot(r22) + A032.dot(r33)
print(f"yh je {yh}")

# treci redovi matrica transformacije A01, A02, A03
A013 = np.array([A01[2][0],A01[2][1],A01[2][2]])
A023 = np.array([A02[2][0],A02[2][1],A02[2][2]])
A033 = np.array([A03[2][0],A03[2][1],A03[2][2]])
zh = A013.dot(r11) + A023.dot(r22) + A033.dot(r33)

print()

print(f"xh je {rh[0][0]}")
print(f"yh je {rh[1][0]}")
print(f"zh je {rh[2][0]}")

# izracunavanje ojlerovih uglova preko matrice transformacije A03. Matrica transformacije je data u 3.53 i 4.106 u zbirci zadataka iz mehanike robota

teta = m.acos(A03[2][2])
print(f"Ojlerov Ugao teta je: {np.around(teta, 4)} rad")

fi = m.asin(A03[2][0]/m.sqrt(1-m.cos(teta)**2))
print(f"Ojlerov Ugao fi je: {np.around(fi, 3)} rad")

psi = m.asin(A03[0][2]/m.sqrt(1-m.cos(teta)**2))
print(f"Ojlerov Ugao psi je: {np.around(psi, 3)} rad")

# Sada su

q4nadvuceno = lamda1 = m.sin(teta/2)*m.cos((psi-fi)/2)
q5nadvuceno = lamda2 = m.sin(teta/2)*m.sin((psi-fi)/2)
q6nadvuceno = lamda3 = m.cos(teta/2)*m.cos((psi+fi)/2)

print(f" spoljasnja koordinata q1nadvuceno = xh = {np.around(rh[0][0], 3)} m\n")
print(f" spoljasnja koordinata q2nadvuceno = yh = {np.around(rh[1][0], 3)} m\n")
print(f" spoljasnja koordinata q3nadvuceno = xh = {np.around(rh[2][0], 3)} m\n")
print(f" spoljasnja koordinata q4nadvuceno = lamda1 = {np.around(q4nadvuceno, 3)} rad\n")
print(f" spoljasnja koordinata q5nadvuceno = lamda2 = {np.around(q5nadvuceno, 3)} rad\n")
print(f" spoljasnja koordinata q6nadvuceno = lamda3 = {np.around(q6nadvuceno, 3)} rad\n")