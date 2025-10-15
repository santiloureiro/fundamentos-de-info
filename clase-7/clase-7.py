# Ejemplo N°4

def imprimirLista(vec):
        largo = len(vec)
        # for number in vec:
        #     print(number, end=" ") 
        for i in range(largo):
             print(vec[i], end=" ")
         
        print()

v = []
n = int(input("Ingreso Num:"))

while n != -1: 
    v.append(n) 
    n = int(input("Ingreso Num nuevo:"))

if len(v) == 0:
    print("Lista Vacia!")
    
else:
    mayor = v[0]
    pos = 0
    for i in range(len(v)):
        if v[i] > mayor:
            mayor = v[i]
            pos = i
    
    imprimirLista(v)

    print(mayor, pos)

    del v[pos]

    imprimirLista(v)
