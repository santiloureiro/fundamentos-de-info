# Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. 
# El fin de la carga se determina ingresando un -1 en el legajo. 
# Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. 
# Se debe validar que la nota ingresada sea entre 1 y 10. 
# Terminada la carga de datos, informar: 
#   > Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
#   > Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
#   > Porcentaje de alumnos que están aplazados (tienen 1 en el examen)

minNota = 1
maxNota = 10

legajo = input("Ingresar legajo de alumno: ")
nota = int(input("Ingresar nota: "))
tablaNotas = ""
alumnosAprobados = 0
alumnosDesaprobados = 0
alumnosAplazados = 0
cantAlumnos = 0
totalNotas = 0


while legajo != "-1":
    if nota >= minNota and nota <= maxNota:
        cantAlumnos += 1
        tablaNotas += f"{legajo}: {nota}\n"
        if nota >= 4:
            alumnosAprobados += 1
        elif nota == 1:
            alumnosAplazados += 1
            alumnosDesaprobados += 1
        else:
            alumnosDesaprobados += 1
        legajo = input("Ingresar nuevo legajo o terminar con -1: ")
        if legajo != "-1":
            nota = int(input("Ingresar nota: "))
    else:
        nota = int(input("Nota invalida, Ingresar otra nota: "))

print("Alumnos totales:", cantAlumnos)
print("Tabla de notas:\n", tablaNotas)
print("Alumnos aprobados:\n", alumnosAprobados)
print("Alumnos desaprobados:\n", alumnosDesaprobados)
print("Alumnos aplazados:\n", alumnosAplazados)
print("Porcentaje de alumnos aplazados:\n", (alumnosAplazados / cantAlumnos) * 100,"%")
