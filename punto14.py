#14. Escribir una función que calcule la media aritmética de una lista de números.
lst = [18, 90, 43, 5, 40, 9, 53, 89, 38, 91]

def mean(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    mn = sum/len(lst)
    return mn


