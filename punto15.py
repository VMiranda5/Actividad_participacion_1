#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no
string = input("ingrese una cadena de texto: ")
string = string.replace(" ", "")
string2 = string[::-1]

if string == string2:
    print("la cadena de texto es palindroma")
else:
    print("la cadena de texto no es palindroma")