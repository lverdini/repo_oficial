<<<<<<< Updated upstream
# Declarar e Inicializar - opcion 1
# matriz = [
#     [1, 3, 2],
#     [3, 5, 1]
# ]

# Declarar e Inicializar - opcion 2
# matriz = []
# fila1 = [1, 3, 2]
# fila2 = [3, 5, 1, 5]
# matriz.append(fila1)
# matriz.append(fila2)
# print(matriz)

# Iterar una lista (puede ser una fila de una matriz)
fila1 = [1, 3, 2]
# Iterar con range
# for i in range(len(fila1)):
#     print(fila1[i])

# Iterar con for .. in
# for f in fila1:
#     print(f)

# Iterar con Enumerate
""" enumerate recibe una lista
    retorna una tupla, formada por:
    - indice
    - valor
"""
for i, f in enumerate(fila1):
    print(f"Indice: {i+1}: Valor: {f}")
=======

matriz = [
    [1, 2, 3],
    [4, 5, 6]

]

print matriz [0][0]  # Imprime el primer elemento de la primera fila (1)


matriz = [ ]

fila1 = [1, 2, 3]
fila2 = [4, 5, 6]

#append agrega un elemento al final de la lista
matriz.append(fila1)
matriz.append(fila2)

print matriz[1][2]  # Imprime el tercer elemento de la segunda fila (6)

# como funciona la matriz? 
# la matriz es una lista de listas, donde cada lista interna representa una fila de la matriz.
# para acceder a un elemento de la matriz, se utiliza el índice de la fila y el índice de la columna. Por ejemplo, matriz[0][1] accede al segundo elemento de la primera fila (2).
# el mejor ejemplo para entenderlo es pensar en una tabla, donde cada fila es una lista y cada columna es un elemento de esa lista.
>>>>>>> Stashed changes
