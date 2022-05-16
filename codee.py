from math import*
import random


print(' ============================') 
print('|                            |')
print('| Bem-vindo ao Insper Países |')
print('|                            |')
print('==== Design de Software ====') 
print('Comandos:')
print('dica       - entra no mercado de dicas')
print('desisto    - desiste da rodada')
print('inventario - exibe sua posição')
print('Um país foi escolhido, tente adivinhar!')



def sorteia(dic):

    lista1 = list(dic.keys())

    ordem = random.choice(lista1)  

    return ordem

def normaliza(x):
    dicc = {}

    for cont in x:
        for paises in x[cont]:
            dicc[paises] = x[cont][paises]
            dicc[paises]['continente'] = cont

    return dicc


def esta_na_lista(pais, lis):
    esta_na_lista = 0
    for i in lis:
        if pais == i[0]:
            esta_na_lista = 1
    if esta_na_lista == 1:
        return True
    else:
        return False
    
def adicionaordem(resp,x,listaa):
    total=0
    pais=[resp, x]
    for x in listaa:
        if x>x[1]:
            total+=1
            listaa.insert(total, pais)
            return listaa

def sorteia(p,k):  

    list = []
    a = ['.', ',', '-', ';', ' ']

    for i in range(len(p)):

        if p[i] not in a and p[i] not in k:

            list.append(p[i])

    x = random.choice(list)

    return x

def haversine (R, l1, y1, l2, y2):

   var1 = sin ( ( ( l2-l1 ) /2 ) *( pi / 180 ) ) ** 2

   var2 = cos (l1* (pi /180 ) )

   var3 = cos( l2 * (pi /180 ) )

   var4 = sin ( ( ( y2-y1 ) /2 ) * ( pi / 180 ) ) ** 2

   dist = 2 * R * asin ( ( var1 + var2 * var3 * var4 ) ** 0.5 )
   
   return dist



while tentou: 
  tentativas=20
  while tentativas>0:
    