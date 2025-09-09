# Se desea analizar cuántos autos circulan con patente con numeración par y cuántos con numeración impar en un día. 
# Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe cuántos vehículos pasaron con numeración par y cuántos con numeración impar.

terminacionPatente = int(input("Ingresar ultimo dijito de la primera patente:"))
contadorPatentesImpares = 0
contadorPatentesPares = 0

while terminacionPatente != -1:
        if(terminacionPatente >= 0 and terminacionPatente <= 9):
            if (terminacionPatente % 2 == 0): 
                contadorPatentesPares = contadorPatentesPares + 1
                terminacionPatente = int(input("Ingresar ultimo dijito de una nueva patente:"))
            else:
                contadorPatentesImpares = contadorPatentesImpares + 1
                terminacionPatente = int(input("Ingresar ultimo dijito de una nueva patente:"))
        else:
            terminacionPatente = int(input("Numero invalido | Ingresar nuevo digito de patente:"))



print("La cantidad de patentes pares es:",contadorPatentesPares)
print("La cantidad de patentes impares es:",contadorPatentesImpares)