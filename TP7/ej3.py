def crearLista(minimo, maximo):
    lista = []
    n = int(input("Ingresar Numero: "))

    while n != -1:
        if(n < minimo or n > maximo):
            n = int(input("Numero fuera de rango | Ingresar nuevo numero: "))
        else:
            lista.append(n)
            n = int(input("Ingresar nuevo numero: "))
    return lista

def esPalindromo (lista):
    listaLength = len(lista)
    ultimoIndice = listaLength - 1
    esCapicua = True
    for i in range(listaLength):
        if(lista[i] != lista[ultimoIndice]):
            esCapicua = False
        ultimoIndice = ultimoIndice - 1 
    return(esCapicua)


lista = crearLista(1,2000)
    
print("La lista es:", lista, "y el resultado del test es:", esPalindromo(lista))