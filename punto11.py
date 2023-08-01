#11. Crear un programa que genere una lista de números pares entre 1 y 100.
lst = []
for i in range(2,101):
    if i%2 == 0:
        lst.append(i)