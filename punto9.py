#9 Crear un programa que genere una matriz de números y la imprima en pantalla.
import random

rows = 2
columns = 2
lower_limit = 1
upper_limit = 100
matrix = []

#creating the matrix
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(random.randint(lower_limit,upper_limit))
    matrix.append(row)

#printing the matrix
for i in range(rows):
    print(matrix[i])
