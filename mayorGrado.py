import numpy as np

#matriz
matriz = np.array([
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0]
])

#conexiones de cada nodo
conexiones = np.sum(matriz, axis=1)


#determinar el mayor
mayor = np.argmax(conexiones)


print("El nodo con mayor numero de conexiones es el nodo numero "+str(mayor+1)," con ",conexiones[mayor]," conexiones.")
