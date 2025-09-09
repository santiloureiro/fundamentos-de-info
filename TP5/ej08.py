# Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3). 
# Por cada empleado se lee su legajo, categoría y salario. 
# Se solicita elaborar un informe que contenga:
#   -Importe total de salarios pagados por la empresa.
#   -Cantidad de empleados que ganan más de $200000.
#   -Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
#   -Legajo del empleado que más gana.
#   -Sueldo más bajo.
#   -Importe total de sueldos por cada categoría.
#   -Salario promedio

legajo = int(input("Ingresar legajo de empleado: "))
salario = int(input("Ingresar salario del empleado: "))
categoria = int(input("Ingresar categoria del empleado: "))
totalSalarios = 0
totalSalarios1 = 0
totalSalarios2 = 0
totalSalarios3 = 0
cantSalariosAltos = 0
categoria3SalariosBajos = 0
legajoSalarioMasAlto = ""
legajoSalarioMasBajo = ""
salarioMasAlto = 0
salarioMasBajo = 0
empleadosTotales = 0

while legajo != -1:
    if categoria == 1 or categoria == 2 or categoria == 3:
        if salario > 200000:
            cantSalariosAltos = cantSalariosAltos + 1
        if salario < 50000 and categoria == 3:
            categoria3SalariosBajos = categoria3SalariosBajos + 1
        if salario > salarioMasAlto:
            salarioMasAlto = salario
            legajoSalarioMasAlto = legajo
        if salario < salarioMasBajo or salarioMasBajo == 0:
            salarioMasBajo = salario
            legajoSalarioMasBajo = legajo
        if categoria == 1:
            totalSalarios1 = totalSalarios1 + salario
        elif categoria == 2:
            totalSalarios2 = totalSalarios2 + salario
        else:
            totalSalarios3 = totalSalarios3 + salario
        totalSalarios = totalSalarios + salario
        empleadosTotales = empleadosTotales + 1
        print("✅ | Empleado Registrado!")
        legajo = int(input("Ingresar un nuevo legajo de empleado o -1 para terminar el registro: "))
        if legajo != -1:
            categoria = int(input("Ingresar categoria del empleado: "))
            salario = int(input("Ingresar salario del empleado: "))
    else:
        categoria = int(input("La categoria es invalida | Ingresar categoria (1 | 2 | 3):"))
            

print("👥 | Cantidad de empleados: ", empleadosTotales)
print("💵 | Importe total de salarios en la empresa: ", totalSalarios)
print("💵 | Importe total de salarios en la categoria 1: ", totalSalarios1)
print("💵 | Importe total de salarios en la categoria 2: ", totalSalarios2)
print("💵 | Importe total de salarios en la categoria 3: ", totalSalarios3)
print("💵 | Salario promedio: ", totalSalarios / empleadosTotales)
print("💵 | El empleado que mas gana es: ", legajoSalarioMasAlto, "y gana: ", salarioMasAlto)
print("💵 | El salario del empleado que menos gana es:", salarioMasBajo)