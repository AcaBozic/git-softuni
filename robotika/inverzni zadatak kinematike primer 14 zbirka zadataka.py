# zadatak se referencira na podatke iz zbirke zadataka strana 109 primer 14

# ovaj zadatak mi nije jasan ne mogu ga resiti....

import numpy as np
import math as m

l1 = float(input("Unesi duzinu segmenta robotske ruke l1: "))
l3 = float(input("Unesi duzinu segmenta robotske ruke l3: "))

q1 = float(input("Unesi pocetnu vrednost generalisane koordinate q1: "))
q2 = float(input("Unesi pocetnu vrednost generalisane koordinate q2: "))
q3 = float(input("Unesi pocetnu vrednost generalisane koordinate q3: "))

q1d = float(input("Unesi pocetnu vrednost generalisane brzine q1d: "))
q2d = float(input("Unesi pocetnu vrednost generalisane brzine q2d: "))
q3d = float(input("Unesi pocetnu vrednost generalisane brzine q3d: "))


# for i in range(10):
    q = np.array([[q1],
                  [q2],
                  [q3]])

    qspodz = m.sqrt(2) / 2
    qsdodx = 4/5*qspodz
    qspody = 3/5*qspodz

    qspod = np.array([[qsdodx],
                      [qspody],
                      [qspodz]])

    qd = np.array([[q1d],
                   [q2d],
                   [q3d]])

    xhd = m.cos(q1)*(l1+m.sin(q2)*(l3+q3))*q1d + m.sin(q1)*(m.cos(q2)*(l3+q3)*q2d + m.sin(q2)*q3d)
    yhd = -m.sin(q2)*(l3+q3)*q2d + m.cos(q2)*q3d
    zhd = -m.sin(q1)*(l1+m.sin(q2)*(l3+q3))*q1d + m.cos(q1)*((l3+q3)*m.cos(q2)*q2d + m.sin(q2)*q3d)

    Q = np.array([[xhd],
                  [yhd],
                  [zhd]])

    j11 = m.cos(q1)*(l1+m.sin(q2)*(l3+q3))
    j21 = 0
    j31 = -m.sin(q1)*(l1+m.sin(q2)*(l3+q3))
    j12 = m.sin(q1)*m.cos(q2)*(l3+q3)
    j22 = -m.sin(q2)*(l3+q3)
    j32 = m.cos(q1)*(l3+q3)*m.cos(q2)
    j13 = m.sin(q1) * m.sin(q2)
    j23 = m.cos(q2)
    j33 = m.cos(q1) * m.sin(q2)
    J = np.array([[j11, j12, j13],
                  [j21, j22, j23],
                  [j31, j32, j33]])
    print(J)
    print()
    print(np.linalg.inv(J))
    a = np.linalg.inv(J).dot(qspod)

    # print(f"\nOvo je {i + 1} iteracija\n")
    # eps = a - qd
    # print(f"Greska pri izracunavanju je:\n {eps}\n")
    print(f"vrednosti unutrasnjih koordinata su: \n {a}\n")
    q1d = a[0][0]
    q2d = a[1][0]
    q3d = a[2][0]