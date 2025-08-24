precio = int(input("Ingresar precio del medicamento:"));
descuento = 35

print("El precio del medicamento es: $",precio);
print("El descuento a aplicar es:", descuento, "%");
print("El precio final a pagar es:", precio - (precio * round(35*0.01,2)));