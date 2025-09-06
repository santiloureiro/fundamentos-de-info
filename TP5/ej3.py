# Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
#   >Aplica el precio base a la primera docena de unidades.
#   >Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#   >Aplica un 25% de descuento a todas las unidades por encima de las 100.
# 
# Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:
#   >100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04
# 
# Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar:
#   >Cantidad de ventas realizadas total.
#   >Cantidad de ventas en las que se aplicó un 10% de descuento.
#   >Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.

cantProductos = int(input("Ingresar cantidad de productos: "))
precioBase = int(input("Ingresar precio del producto: "))
precio10 = precioBase - (precioBase * 0.10)
precio25 = precioBase - (precioBase * 0.25)
cantidadACobrar = 0
cantidadDeVentas = 0
cantidadDeVentasDescuento10 = 0
cantidadDeVentasBase = 0
while cantProductos != -1:
    cantidadACobrar = 0
    iterador = 0
    cantidadDeVentas += 1
    if cantProductos <= 12:
        cantidadDeVentasBase += 1
    if cantProductos > 12:
        cantidadDeVentasDescuento10 += 1
    while iterador < cantProductos:
        if iterador <= 12:
            cantidadACobrar += precioBase
        if iterador > 12 and iterador <= 100:
            cantidadACobrar += precio10
        if iterador > 100:
            cantidadACobrar += precio25
        iterador += 1
    print("Compra Num: ", cantidadDeVentas)
    print("Cantidad de productos: ", cantProductos)
    print("Precio a pagar: ", cantidadACobrar)
    print("Precio base: ", precioBase)
    print("Precio a partir de 13 unidades hasta 100: ", precio10)
    print("Precio a partir de las 100 unidades: ", precio25)
    cantProductos = int(input("Ingresar cantidad de productos o -1 para finalizar: "))
    if cantProductos != -1:
        precioBase = int(input("Ingresar precio del producto: "))

print("\nTotal de ventas:", cantidadDeVentas)
print("Total de ventas con 10% de descuento aplicado:", cantidadDeVentasDescuento10)
print("Total de ventas sin descuento:", cantidadDeVentasBase)