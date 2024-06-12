import numpy as np
import math as m

psi = float(input("Unesi ugao rotacije psi oko z ose: "))
tetak = float(input("Unesi ugao rotacije teta oko n ose: "))
fi = float(input("Unesi ugao rotacije fi oko ni ose: "))

teta1 = np.array([[0],[2*m.sin(m.radians(tetak))*m.tan(m.radians(psi/2))],[2*m.cos(m.radians(tetak))*m.tan(m.radians(psi/2))]])
teta2 = np.array([[2*m.tan(m.radians(tetak/2))],[0],[0]])
teta3 = np.array([[0],[0],[2*m.tan(m.radians(fi/2))]])

teta23 = np.array([[2*m.tan(m.radians(tetak/2))],[2*m.tan(m.radians(tetak/2))*m.tan(m.radians(fi/2))],[2*m.tan(m.radians(fi/2))]])

# ugao konacne rotacije
teta = np.array([[2*m.tan(m.radians(tetak/2))],[2*m.tan(m.radians(tetak/2))*m.tan(m.radians((psi+fi)/2))],[2*m.tan(m.radians((psi+fi)/2))]])

# stampanje matrice vektora ugla konacnog slaganja rotacija za uglove psi, tetak i fi (ojlerovi uglovi). Stampa na 4 decimale.
print(np.around(teta,4))
