n = int(input("Ingrese un número o -1 para terminar:"))

mayor = n

while n != -1:
    if n > mayor:
        mayor = n
    n = int(input("Ingrese un nuevo numero o -1 para terminar:"))
print("El numero mas grande es:", mayor)