# Escribir un programa en Python que: 
# Permita ingresar al usuario las notas de los alumnos de un curso:
# Serán números enteros entre 1 y 10.
# El ingreso de las notas finaliza con -1.
# Una vez finalizada la carga se pide Informar:
#      - Cuántos alumnos aprobaron el examen. (nota >=4).
#      - Cuántos alumnos reprobaron el examen. (nota <4).
#      - Cuál fue la mayor nota
#      - Cual fue la menor nota
#      - Cantidad total de exámenes
#      - La posición de la mayor nota
#      - La posición de la menor nota


nota = int(input("Ingresar nota del primer alumno:"))

cantNotas = 0
cantAprobados = 0
cantReprobados = 0

menorNota = 0
indiceMenorNota = 0

mayorNota = 0
indiceMayorNota = 0

# Carga notas hasta que el usuario ingrese -1 para terminar el registro
while nota != -1:
    # Checkea si las notas cargadas son validas (>= 1 y <= 10)
    if nota <= 10 and nota >= 1:
        cantNotas += 1
        if nota >= 4:
            cantAprobados += 1
        else: 
            cantReprobados += 1
        # Registra una nueva menor o mayor nota
        if nota > mayorNota:
            mayorNota = nota            
            indiceMayorNota = cantNotas 
        if nota < menorNota or menorNota == 0:
            menorNota = nota
            indiceMenorNota = cantNotas

        nota = int(input("Ingresar nueva nota de alumno o -1 para terminar la carga: "))
    else:
        nota = int(input("NOTA INVALIDA | Ingresar nueva nota de alumno o -1 para terminar la carga: "))

print("La cantidad de examenes fue: ", cantNotas)
print("La cantidad de aprobados fue: ", cantAprobados)
print("La cantidad de desaprobados fue: ", cantReprobados)
print("La mayor nota fue del alumno: ", indiceMayorNota , "y sacó", mayorNota)
print("La menor nota fue del alumno: ", indiceMenorNota , "y sacó", menorNota)
