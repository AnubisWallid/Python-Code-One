'''
Questão 1.
Faça um programa que peça ao usuário um número e imprima todos os números de um até o
número que o usuário informar.

'''
numero = int(input("Digite um numero para gerar a sequência:"))
numero += 1

for i in range(numero):
    print(i)