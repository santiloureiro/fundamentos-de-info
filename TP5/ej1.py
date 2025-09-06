# 1. Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válida una edad entre 0 y 100).

minEdad = 0
maxEdad = 100

edad = int(input("Ingresar edad: "))
personasMayores18 = 0
personasMenores18 = 0
cantPersonas = 0
totalEdades = 0


while edad != -1:
    if edad >= minEdad and edad <= maxEdad:
        cantPersonas += 1
        if edad < 18:
            personasMenores18 += 1
        else:
            personasMayores18 += 1
        edad = int(input("Ingresar nueva edad o terminar con -1: "))
    else:
        edad = int(input("Edad invalida, Ingresar otra edad: "))

print("Personas totales:", cantPersonas)
print("Personas mayores a 18:", personasMayores18)
print("Personas menores a 18:", personasMenores18)
print("El promedio de edades es", totalEdades // cantPersonas)
