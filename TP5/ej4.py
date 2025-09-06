# Una empresa factura a sus clientes el último día de cada mes. 
# Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
# Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura, mientras que si paga después del día 20 deberá abonar una multa de $350 o del 10% de su factura, lo que resulte mayor. 
# Escribir un programa que lea el número del cliente y el total de la factura, y emita un informe donde conste el número del cliente y los tres importes que podría abonar según la fecha de pago.

cliente = input("Ingresar ID de cliente: ")
precioBase = int(input("Ingresar monto de la factura: "))
precioAnticipado = precioBase - 200 
precio20dias = precioBase + 350

descuentoAdelantado = precioBase - (precioBase * 0.02)
aumentoAtrasado = precioBase + (precioBase * 0.1)

if precioAnticipado <= 0:
    precioAnticipado = 0
if precioAnticipado > descuentoAdelantado:
    precioAnticipado = descuentoAdelantado
if precio20dias < aumentoAtrasado :
    precio20dias = aumentoAtrasado

print("ID CLIENTE:", cliente)
print("Precio a pagar del 1 al 10:", precioAnticipado)
print("Precio factura hasta el 20:", precioBase)
print("Precio factura vencida:", precio20dias)