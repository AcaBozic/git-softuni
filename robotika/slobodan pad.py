import numpy as np
import matplotlib.pyplot as plt

def dv_dt(v):
    return g-(k/m)*v**2

m = 80 
k = 0.24
g = 9.81
t0 = 0
v0 = 0
tf = 30
n = 21

t = np.linspace(t0,tf,n)
v = np.zeros(n)

h = (tf-t0)/(n-1)

t[0] = t0
v[0] = v0

for i in range (0,n-1):
    v[i+1]= v[i] + h * dv_dt(v[i])

plt.plot(t,v)
plt.title("Slobodan pad sa silom otpora sredine")
plt.xlabel("Vreme [s]")
plt.ylabel("Brzina [m/s]")
plt.show()