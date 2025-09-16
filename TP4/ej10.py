# El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X tales que 0 < X <= N.
# Desarrollar un programa para calcular el factorial de un número dado. 
# Deberán rechazarse las entradas inválidas (menores que 0)

numero = int(input("Ingresar numero a calcular factorial: "))

numeroPrevio = 1
contador = 0
factorialAcc = 0
while numero < 0 :
     numero = int(input("Numero invalido | Ingresar un nuevo numero valido a calcular factorial: "))

while contador < numero :
     factorialAcc = factorialAcc + (contador * numeroPrevio)
     numeroPrevio = numeroPrevio + 1
     contador = contador + 1
     print(factorialAcc)

print(factorialAcc)