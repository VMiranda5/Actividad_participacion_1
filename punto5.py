#5. Crear una función que convierta grados Fahrenheit a grados Celsius.
def f_to_c(f_num):
    c_num = (f_num - 32)*(5/9)
    return c_num

print(f_to_c(90))