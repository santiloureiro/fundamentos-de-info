# Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y un número entero N que representa una cantidad de días. 
# Realizar un programa que imprima la nueva fecha que resulta de sumar N días a la fecha dada. 
# Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3.

# Un año es bisiesto cuando es divisible por 4.
# Aquellos años que sean divisibles por 4 y también por 100 no son bisiestos
# A menos que también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el 2000

dia = int(input("Ingresar dia:"))
mes = int(input("Ingresar mes:"))
año = int(input("Ingresar año:"))
cantDias = int(input("Cantidad de dias de diferencia:"))
diasRestantes = cantDias
diasAFinalizarMes = 0
# Cantidad de dias por meses
enero = 31
febrero = 29
marzo = 31
abril = 30
mayo = 31
junio = 30
julio = 31
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

# Cambiar de bisiesto a año normal
if (mes % 4 != 0) or (mes % 4 == 0 and mes % 100 == 0):
    febrero = 28
print("Fecha original: ", dia, "de ", mes, "de ", año)
while diasRestantes > 0:
    checkearCambioDeMes = (mes == 1 and dia == enero) or (mes == 2 and dia == febrero) or (mes == 3 and dia == marzo) or (mes == 4 and dia == abril) or (mes == 5 and dia == mayo) or (mes == 6 and dia == junio) or (mes == 7 and dia == julio) or (mes == 8 and dia == agosto) or (mes == 9 and dia == septiembre) or (mes == 10 and dia == octubre) or (mes == 11 and dia == noviembre) 
    if(mes == 12 and dia == diciembre):
        dia = 1
        mes = 1
        año = año + 1
    if checkearCambioDeMes:
        dia = 1
        mes = mes + 1 
    else:
        dia = dia + 1
    
    diasRestantes = diasRestantes - 1
       
print("Fecha nueva: ", dia, "de ", mes, "de ", año)


