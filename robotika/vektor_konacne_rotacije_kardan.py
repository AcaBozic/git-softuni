import numpy as np
import math as m

#Sabiranje konacnih rotacija, strana 61 do 63 zbirka zadataka iz mehanike robota, M.Lazarevic

alfa = float(input("Uneti ugao rotacije oko z ose: "))
beta = float(input("uneti ugao rotacije oko x ose: "))

#  projekcije vektora na ose nepomicnog koordinatnog sistema
print("projekcije vektora na ose nepomicnog koordinatnog sistema: \n")

teta1 = np.array([[0],[0],[2*m.tan(m.radians(alfa/2))]])
print (teta1)
print ("\n")


teta2= np.array([[2*m.tan(m.radians(beta/2))*m.cos(m.radians(alfa))], [2*m.tan(m.radians(beta/2))*m.sin(m.radians(alfa))],[0]])
print (teta2,"\n")

#  Rezultujuci vektor konacne rotacije koji prevodi kuto telo sa kardanovim zglobom iz pocetnog u krajnji polozaj

print("Rezultujuci vektor konacne rotacije koji prevodi kuto telo sa kardanovim zglobom iz pocetnog u krajnji polozaj: \n")
tetarez = np.array([[2*m.tan(m.radians(beta/2))],[2*m.tan(m.radians(beta/2))*m.tan(m.radians(alfa/2))],[2*m.tan(m.radians(alfa/2))]])
print (tetarez,"\n")

#  Intenzitet vektora konacne rotacije

print("Intenzitet vektora konacne rotacije:\n")
tetaintenz = m.sqrt((2*m.tan(m.radians(beta/2)))**2 + (2*m.tan(m.radians(beta/2))*m.tan(m.radians(alfa/2)))**2 + (2*m.tan(m.radians(alfa/2)))**2)
print(tetaintenz,"\n")

# tetaintenz = 2*m.tan(gama/2)
# Ugao konacne rotacije vektora konacne rotacije

print("Ugao konacne rotacije vektora konacne rotacije: \n")
gama = 2*m.atan(tetaintenz/2)
print(m.degrees(gama), "\n")

# e0 = 1/(2*m.tan(gama/2))*tetarez
# jedinacni vektor konacne rotacije

print("jedinacni vektor konacne rotacije: \n")
e0 = 1/tetaintenz*tetarez
print(e0)