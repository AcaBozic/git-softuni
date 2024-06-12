import numpy as np
import math as m


q1 = float(input("Unesi pocetnu vrednost q1: "))
q2 = float(input("Unesi pocetnu vrednost q2: "))
q3 = float(input("Unesi pocetnu vrednost q3: "))

q1spo = float(input("Unesi vrednost spoljasnje koordinate q1: "))
q2spo = float(input("Unesi vrednost spoljasnje koordinate q2: "))
q3spo = float(input("Unesi vrednost spoljasnje koordinate q3: "))

for i in range (10):

    q = np.array([[q1],
                  [q2],
                  [q3]])

    qspo = np.array([[q1spo],
                     [q2spo],
                     [q3spo]])

    xh = -(1+q3)*m.sin(q1)*m.cos(q2)
    yh = (1+q3)*m.cos(q1)*m.cos(q2)
    zh = 0.8+(1+q3)*m.sin(q2)

    Q = np.array([[xh] ,
                  [yh] ,
                  [zh]])

    j11 = -(1 + q3) * m.cos(q1) * m.cos(q2)
    j21 = -(1 + q3) * m.cos(q2) * m.sin(q1)
    j31 = 0
    j12 = (1 + q3) * m.sin(q1) * m.sin(q2)
    j22 = -(1 + q3) * m.cos(q1) * m.sin(q2)
    j32 = (1 + q3) * m.cos(q2)
    j13 = -m.sin(q1) * m.cos(q2)
    j23 = m.cos(q2) * m.cos(q1)
    j33 = m.sin(q2)
    J = np.array([[j11 , j12 , j13],
                  [j21 , j22 , j23],
                  [j31 , j32 , j33]])

    a = q-np.linalg.inv(J).dot(Q-qspo)
    print(f"\nOvo je {i+1} iteracija\n")
    eps = a-q
    print(f"Greska pri izracunavanju je:\n {eps}\n")
    print(f"vrednosti unutrasnjih koordinata su: \n {a}\n")
    q1 = a[0][0]
    q2 = a[1][0]
    q3 = a[2][0]








