#13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
sum = num1 + num2
subt = num1 - num2
prod = num1 * num2
print(f"la suma entre {num1} y {num2} es {sum}")
print(f"la resta entre {num1} y {num2} es {subt}")
print(f"el producto entre {num1} y {num2} es {prod}")

if num2 != 0:
    div = num1/num2
    print(f"la division entre {num1} y {num2} es {div}")
else:
    print("ingrese un segundo numero diferente de cero para la division")
