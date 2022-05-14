'''
Questão 9.
Crie (manualmente ou sorteando os números) uma lista de 10 números e imprima:
1. uma lista com os 4 primeiros números;
2. uma lista com os 5 últimos números;
3. uma lista contendo apenas os elementos das posições pares;
4. uma lista contendo apenas os elementos das posições ímpares;
5. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
6. uma lista inversa dos 5 primeiros números;
7. uma lista inversa dos 5 últimos números.
'''
import random

lista = []

for i in range(10):
    lista.append(random.randint(1,10))

print(lista)
print("1.",lista[0:4])
print("2.",lista[5:])
print("3.",lista[0::2])
print("4.",lista[1::2])
lista.reverse()
print("5.",lista)
print("6.",lista[0:4])
print("7.",lista[5:])


