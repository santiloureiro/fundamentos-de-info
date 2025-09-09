# Un complejo de cines necesita un programa para contabilizar el dinero que recauda. 
# Por cada función se ingresa la cantidad de espectadores y si esa función tiene descuento o no (1=Sí, 2=No). 
# La carga finaliza cuando la cantidad de espectadores sea igual a cero. 
# En ese momento el programa deberá:
#   Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $3500 en los días de descuento $5000 en los días sin descuento.
#   Determinar cuántos espectadores ingresaron con descuento y qué porcentaje representan sobre el total de funciones.


precioDescuento = 3500
precio = 5000

espectadoresInput = int(input("Ingresar cantidad de espectadores de la primera funcion (0 para terminar): "))
espectadoresSinDescuento = 0
espectadoresDescuento = 0
recaudacionTotal = 0
descuento = int(input("Tiene descuento? 1=Si 2=No "))

while espectadoresInput != 0:
    while not (descuento == 1 or descuento == 2):
        descuento = int(input("Numero invalido | Tiene descuento? 1=Si 2=No"))
    if(descuento == 1):
        espectadoresDescuento = espectadoresDescuento + espectadoresInput
        recaudacionTotal = recaudacionTotal + (precioDescuento * espectadoresInput)
        print("✅ Funcion guardada con exito!")
        espectadoresInput = int(input("Ingresar cantidad de espectadores de la siguente funcion (0 para terminar): "))
        if(espectadoresInput != 0):
            descuento = int(input("Tiene descuento? 1=Si 2=No "))
    elif(descuento == 2):
        espectadoresSinDescuento = espectadoresSinDescuento + espectadoresInput
        recaudacionTotal = recaudacionTotal + (precio * espectadoresInput)
        print("✅ Funcion guardada con exito!")
        espectadoresInput = int(input("Ingresar cantidad de espectadores de la siguente funcion (0 para terminar): "))
        if(espectadoresInput != 0):
            descuento = int(input("Tiene descuento? 1=Si 2=No "))

print("Carga terminada!\n")
print("Cantidad total recaudada: ", recaudacionTotal)
print("Espectadores que entraron con descuento: ", espectadoresDescuento)
print("Espectadores que entraron sin descuento: ", espectadoresSinDescuento)
print("Porcentaje de descuentos: ", (espectadoresDescuento / (espectadoresSinDescuento + espectadoresDescuento))*100,"%")





