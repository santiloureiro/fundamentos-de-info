# Pide un numero para empezar y un numero maximo y loggea todos los numeros en el medio (Incluyendo el 1ero y ultimo)
startNumber = int(input("Enter number to start from:"));
maxNumber = int(input("Enter max number:"))

while startNumber <= maxNumber:
    print(startNumber)
    startNumber+= 1;