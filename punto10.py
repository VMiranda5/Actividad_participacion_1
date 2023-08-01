#10. Escribir una función que calcule el factorial de un número dado.
n = int(input("ingrese un numero: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f'el factorial de {n} es {fact}')