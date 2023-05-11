import numpy as np
import matplotlib.pyplot as plt
import random

xMax = 10
yMax = 10

# Tablero a cero
tablero = np.zeros((xMax+2,yMax+2),dtype=int)
t_aux   = np.zeros((xMax+2,yMax+2),dtype=int)
v = 0

# Relleno tablero
for j in range(xMax):
    for i in range(yMax):
        tablero[j+1,i+1] = random.randint(0,1)

def Actualizo():
    for j in range(1,xMax+1):
        for i in range(1,yMax+1):
            v = tablero[j,i+1] + tablero[j,i-1] + tablero[j+1,i] + tablero[j-1,i] + tablero[j-1,i+1] + tablero[j-1,i-1] + tablero[j+1,i+1] + tablero[j+1,i-1]
            #t_aux[j,i] = v
            if ((tablero[j,i] == 1) and (v==2 or v==3)) or ((tablero[j,i] == 0) and (v==3)):
                t_aux[j,i]=1
            else:
                t_aux[j,i]=0

Actualizo()

print(tablero)
print(t_aux)

#plt.imshow(tablero,cmap="gray")
#plt.show()
