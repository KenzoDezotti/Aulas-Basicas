from turtle import shape
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd




def GeraMatriz(matriz, passo = 2, janela = 4):
    matriz_final = np.zeros(shape=(1,1))
    distancia = matriz.size*janela//passo
    contador = 0
    for i in range(0,distancia):
        x = [] 
        for j in range(janela):
                x.append(matriz[j+contador])
        contador+=passo
        print(x)
        np.append(matriz_final, x)

df = pd.read_csv("/home/kenzo/Desktop/GOOG.csv")
matriz = np.array(df)
print(matriz)



#plt.scatter(matriz,mat)
#plt.show()









