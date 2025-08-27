# testVar = int(input("Ingrese un numero:"));

# if testVar == 2:
#     print("la variable es 2!")
# else:
#     print("la variable no es 2")


# if testVar>5 and testVar < 10:
#     print("El valor esta entre 5 y 10");

# testOr = int(input("Ingresar numero para testeo OR:"))

# if testOr == 1 or testOr == 2:
#     print("El valor es 1 o 2;");

# testNot = int(input("Ingresar Mes:"))

# if not (testNot==1 or testNot==2 or testNot==3):
#     print("El mes no esta en el primer trimestre");
# else:
#     print("El mes esta en el primer trimestre")


# TP3 Ej: 3
# Desarrollar un programa que solicite un numero de mes (por ejemplo 4) 
# y escriba el nombre del mes en letras ("Abril"). 
# Verificar que el mes sea valido y mostrar un mensaje de error en caso que no lo sea.

mes = int(input("Escriba un numero de mes:"))

if mes >= 1 and mes <= 12:
    if mes == 1:
        print("Enero")
    if mes == 2:
        print("Febrero")
    if mes == 3:
        print("Marzo")
    if mes == 4:
        print("Abril")
    if mes == 5:
        print("Mayo")
    if mes == 6:
        print("Junio")
    if mes == 7:
        print("Julio")
    if mes == 8:
        print("Agosto")
    if mes == 9:
        print("Septiembre")
    if mes == 10:
        print("Octubre")
    if mes == 11:
        print("Noviembre")
    if mes == 12:
        print("Diciembre")
else:
    print("El numero de mes es invalido")

# TP3 Ej: 4