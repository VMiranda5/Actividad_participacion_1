#3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

list_length = 10
lower_limit = 1
upper_limit = 100
random_list = []
for i in range(list_length):
    random_list.append(random.randint(lower_limit,upper_limit))

print(random_list)