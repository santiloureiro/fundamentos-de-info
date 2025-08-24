medidaIngresada = int(input("Ingresar centimetros a convertir:"));

medidaPulgadas = medidaIngresada / 2.54;
medidaPies = medidaPulgadas / 12;
medidaYardas = medidaPies / 3;

print("Medida ingresada:", medidaIngresada);
print("Medida en pulgadas", medidaPulgadas);
print("Medida en pies", medidaPies);
print("Medida en yardas", medidaYardas);
