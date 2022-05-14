'''
Questão 6.
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.

'''

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [10,20,30,40,50,60,70,80,90,100]

def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

print("A soma da lista=",soma_lista(lista))
print("A soma da lista=",soma_lista(lista2))