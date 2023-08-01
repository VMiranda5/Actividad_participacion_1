#7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada
lst = [12,64,3,78,23,43,73,2,556,4,6,432,45,53,195,549]
smallest = lst[0]
greatest = lst[0]
for i in lst:
    if smallest > i:
        smallest = i
    if greatest < i:
        greatest = i

print("el numero mas grande es: ", greatest)
print("el numero mas pequeño es: ", smallest)
