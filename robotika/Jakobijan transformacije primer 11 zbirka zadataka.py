import numpy as np
import math as m

# zadatak se oslanja na zadatak 9 iz zbirke zadataka

def unos_vektora():
    vektor = np.empty((3,1),dtype=float)
    for i in range(3):
        vektor[i, 0] = float(input(f"Unesi vrednost {i+1} koordinate vektora: "))
    return vektor

def dualobj(A):
    B = np.array([[0,-A[2,0],A[1,0]],[A[2,0],0,-A[0,0]],[-A[1,0],A[0,0],0]])
    return B


q1 = float(input("Unesi vrednost ugla rotacije prvog segmenta q1: "))
q2 = float(input("Unesi vrednost ugla rotacije drugog segmenta q2: "))
q3 = float(input("Unesi vrednost ugla rotacije treceg segmenta q3: "))

print("Unesi vrednost za vektor r11: ")
r11 = unos_vektora()

print("Unesi vrednost za vektor r22: ")
r22 = unos_vektora()

print("Unesi vrednost za vektor r33: ")
r33 = unos_vektora()

print("Unesi vrednost e1: ")
e1 = unos_vektora()

print("Unesi vrednost e2: ")
e2 = unos_vektora()

print("Unesi vrednost e3: ")
e3 = unos_vektora()


A01 = np.array([[1, 0, 0],[0, m.cos(q1), -m.sin(q1)], [0, m.sin(q1), m.cos(q1)]])
A12 = np.array([[m.cos(q2), 0, m.sin(q2)] , [0, 1, 0] , [-m.sin(q2), 0, m.cos(q2)]])
A23 = np.array([[1, 0, 0] , [0, m.cos(q3), -m.sin(q3)] , [0, m.sin(q3), m.cos(q3)]])
A02 = A01.dot(A12)
A03 = A02.dot(A23)
A13 = A12.dot(A23)

# izracunavanje polozaja hvataljke u odnosu na centar 1 segmenta

# prvi kvazibazni vektor koji odgovara vrhu hvataljke, u odnosu na prvi lokalni koordinatni sistem je:

R31 = r11 + A12.dot(r22) + A13.dot(r33)

taun11 = dualobj(e1).dot(R31)
# prvi kvazibazni vektor u odnosu na nepokretni koordinatni sistem je:
taun10 = A01.dot(taun11)

print(f"kvazibazni vektor 1 je:\n {taun10} \n")

# drugi kvazibazni vektor koji odgovara vrhu hvataljke, u odnosu na drugi lokalni koordinatni sistem je:

R32 = r22 + A23.dot(r33)
taun22 = dualobj(e2).dot(R32)
# drugi kvazibazni vektor u odnosu na nepokretni koordinatni sistem je:
taun20 = A02.dot(taun22)

print(f"kvazibazni vektor 2 je:\n {taun20} \n")




# treci kvazibazni vektor koji odgovara vrhu hvataljke, u odnosu na treci lokalni koordinatni sistem je:

R33 = r33
taun33 = dualobj(e3).dot(R33)
# treci kvazibazni vektor u odnosu na nepokretni koordinatni sistem je:
taun30 = A03.dot(taun33)
print(f"kvazibazni vektor 3 je:\n {taun30} \n")

# matrica D se izracunava u odnosu na kvazibazne vektore prvi, drugi i treci

D = np.array([[taun10[0][0] , taun20[0][0] , taun30[0][0]] , [taun10[1][0] , taun20[1][0] , taun30[1][0]] , [taun10[2][0] , taun20[2][0] , taun30[2][0]]])

print(f"Matrica D se moze izracunati i ona je: \n {np.around(D,3)} \n")

# Jakobijanova matrica transformacije se dobija:

J1 = np.identity(3,dtype=float).dot(D)
print(f"Jakobijanova matrica transformacije J1 je: \n {np.around(J1,3)}\n")


# Za odredjivanje J2 potrebno je da znamo matrice transformacija Kit i Kojl i E


teta = m.acos(A03[2][2])
print(f"Ojlerov Ugao teta je: {np.around(teta, 4)} rad")

fi = m.asin(A03[2][0]/m.sqrt(1-m.cos(teta)**2))
print(f"Ojlerov Ugao fi je: {np.around(fi, 3)} rad")

psi = m.asin(A03[0][2]/m.sqrt(1-m.cos(teta)**2))
print(f"Ojlerov Ugao psi je: {np.around(psi, 3)} rad")

Kit = np.array([[-1/2*m.sin(teta/2)*m.sin((psi-fi)/2) , 1/2*m.cos(teta/2)*m.cos((psi-fi)/2) , 1/2*m.sin(teta/2)*m.sin((psi-fi)/2)],
                [1/2*m.sin(teta/2)*m.cos((psi-fi)/2) , 1/2*m.cos(teta/2)*m.sin((psi-fi)/2) , -1/2*m.sin(teta/2)*m.cos((psi-fi)/2)],
                [1/2*m.cos(teta/2)*m.cos((psi+fi)/2) , -1/2*m.sin(teta/2)*m.sin((psi+fi)/2) , 1/2*m.cos(teta/2)*m.cos((psi+fi)/2)]])

Kojl = np.array([[0, m.cos(psi), m.sin(teta)*m.sin(psi)],
                 [0, m.sin(psi), -m.sin(teta)*m.cos(psi)],
                 [1, 0, m.cos(teta)]])

E1 = A01.dot(e1)
E2 = A02.dot(e2)
E3 = A03.dot(e3)

E = np.array([[E1[0][0] , E2[0][0] , E3[0][0]] ,
              [E1[1][0] , E2[1][0] , E3[1][0]] ,
              [E1[2][0] , E2[2][0] , E3[2][0]]])

print(Kit)
print()

Kinv = np.linalg.inv(Kojl)
print(Kinv)
print()

print(E)
print()

J21 = Kinv.dot(E)
J2 = Kit.dot(J21)
print(J2)