invPersona1 = int(input("Ingresar inversion de persona 1:"));
invPersona2 = int(input("Ingresar inversion de persona 2:"));
invPersona3 = int(input("Ingresar inversion de persona 3:"));

invTotal = invPersona1 + invPersona2 + invPersona3;

print("La inversion total es:", invTotal)
print("La primera persona invirtio un", (invPersona1 / invTotal)*100, "%");
print("La segunda persona invirtio un", (invPersona2 / invTotal)*100, "%");
print("La tercera persona invirtio un", (invPersona3 / invTotal)*100, "%");
