def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor

'''ordenada = []

while lista:
    indice = acha_menor(lista)
    elemento = lista.pop(indice)
    ordenada.append(elemento)
    print(lista)
    print(ordenada)
    
    

def selection_short_ruim(lista):    
    for i in range(len(lista)):
        indice_menor = acha_menor(lista[i:]) +i
        aux = lista[i]
        lista[i] = lista[indice_menor]
        lista[indice_menor] = aux
    return 




for j in range(lista):
    n_trocas = 0
    for i in range(len(lista)-1):
        aux = lista[i]
        lista[i] = lista[i +1]
        lista[i+1] =aux
        n_trocas +=1
    if n_trocas ==0:
        break
print(lista)
'''



def raiz_binaria(num,ini,fim):
     if fim - ini <= 0.001:
         chute = (ini+fim)/2
         if chute **2 > num:
             fim = chute
         else:
             ini = chute
         chute = raiz_binaria(num,ini,fim)
     return chute

def verifica_numero(msg):
    num = input(msg)
    if not num.isnumeric():
        num = verifica_numero(msg)
    return int(num)

def quicksort(lista):
    if len(lista) <=1:
    pivo = lista[0]
    menores = [elem for elem in lista if elem < pivo]
    maiores = [elem for elem in lista if elem > pivo]
    menores_ordenada = quicksort(menores)
    maiores_ordenada = quicksort(maiores)
    print(menores,[pivo],maiores)
    return menores_ordenada + [pivo] + maiores_ordenada

lista = [5,3,4,2,8,9,7,10,6,1]


lista = quicksort(lista)
print(lista)