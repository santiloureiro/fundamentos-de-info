# Simular un ahorro de la sig. manera:

# El monto para ahorrar debe ser introducido por teclado 
# Debe estar comprendido entre $80000 y $100000.
# Los depósitos semanales deben ser entre $5000 y $10000 hasta que se iguale o supere el monto a ahorrar.

# Se debe informar: 
# El importe de los depósitos que se hicieron, 
# La cantidad de depósitos que se hicieron, 
# El promedio de depósitos, 
# El mayor depósito efectuado y su posición
# El menor depósito efectuado y su posición.

montoAAhorrar = int(input("Cuanto se quiere ahorrar? "))

# Bucle hasta que el usuario ingrese una cantidad valida para el ahorro (Entre 80.000 y 100.000)
while not (montoAAhorrar > 80000 and montoAAhorrar < 100000):
    montoAAhorrar = int(input("El monto debe estar entre $80.000 y $100.000 | Cuanto se quiere ahorrar? "))

montoAhorro = int(input("Ingresar primer monto a para el ahorro: "))

totalAhorro = 0

cantDepositos = 0

mayorDeposito = 0
indiceMayorDeposito = 0

menorDeposito = 0
indiceMenorDeposito = 0

# Bucle hasta que el usuario detenga el ingreso con -1 o hasta que se pase de 100000
while totalAhorro <= montoAAhorrar and montoAhorro != -1:
    # Checkea si el monto esta dentro del rango de ingresos semanales permitidos (Entre 5000 y 10000)
    if not (montoAhorro > 10000 or montoAhorro < 5000):
        totalAhorro += montoAhorro 
        cantDepositos += 1
        print("Deposito N°",cantDepositos, "| Cantidad: ", montoAhorro)
        # Checkeos para detectar si hay una nueva nota mayor o menor (Tambien se guarda el indice de la misma)
        if montoAhorro > mayorDeposito:
            mayorDeposito = montoAhorro
            indiceMayorDeposito = cantDepositos
        if montoAhorro < menorDeposito or menorDeposito == 0:
            menorDeposito = montoAhorro
            indiceMenorDeposito = cantDepositos
        print("CANTIDAD RESTANTE | ", montoAAhorrar - totalAhorro)
        montoAhorro = int(input("Ingresar nuevo monto de ahorro o salir con -1: "))
    else:
        print("CANTIDAD RESTANTE | ", montoAAhorrar - totalAhorro)
        montoAhorro = int(input("Ingresar nuevo monto valido (entre $5000 y $10000): "))        

promedioDepositos = totalAhorro / cantDepositos

# Reportes
print("Se deposito $",totalAhorro)
print("Se realizaron", cantDepositos, "depositos.")
print("El promedio de los depositos es: ", promedioDepositos)
print("El menor deposito fue:", indiceMenorDeposito, "con $", menorDeposito)
print("El mayor deposito fue:", indiceMayorDeposito, "con $", mayorDeposito)