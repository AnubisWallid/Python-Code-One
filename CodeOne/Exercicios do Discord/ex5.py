'''
Questão 5.
Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
sim ou não:

1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
você vai informar como a polícia o considera.

'''
from re import IGNORECASE


resp1 = input("1. Mora perto da vítima? ")
if resp1.lower() == "sim":
    resp1 = 1
else: resp1 = 0

resp2 = input("2. Já trabalhou com a vítima? ")
if resp2.lower() == "sim":
    resp2 = 1
else: resp2 = 0

resp3 = input("3. Telefonou para a vítima? ")
if resp3.lower() == "sim":
    resp3 = 1
else: resp3 = 0

resp4 = input("4. Esteve no local do crime? ")
if resp4.lower() == "sim":
    resp4 = 1
else: resp4 = 0

resp5 = input("5. Devia para a vítima? ")
if resp5.lower() == "sim":
    resp5 = 1
else: resp5 = 0

soma = resp1 + resp2 + resp3 + resp4 + resp5
print(soma)
if soma == 5:
    print("O suspeito é o ASSASSINO !")
elif soma == 4 or soma == 3:
    print("O suspeito é CUMPLICE.")
elif soma == 2:
    print("É apenas SUSPEITO.")
else:
    print("O suspeito pode ser LIBERADO.")



