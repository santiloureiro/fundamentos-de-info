# Ingresar un número N y validar que sea positivo. 
# Luego:
#   a.Mostrar los primeros números impares, hasta alcanzar el número ingresado.
#   b.Informar la suma de esos números impares.Ejemplo:
#       - Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
#       - Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
#       - Si se ingresa -5, se debe pedir otro número.

numero = int(input("Ingresar un numero positivo: "))
counter = 0
acc = 0

while numero < 0:
    numero = int(input("Numero invalido | Ingresar un numero positivo: "))

while counter <= numero:
    if not(counter % 2 == 0):
        print(counter)
        acc = acc + counter
    counter = counter + 1    
print("El numero ingresado es:", numero)
print("La suma de todos los impares antes del numero es:",acc)





