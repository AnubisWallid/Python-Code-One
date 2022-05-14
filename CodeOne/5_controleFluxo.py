##### Controle de Fluxo
'''
Condicionais:
if(condição): ação 

if(condição):
    ação 
else:
    ação

if(condição):
    ação
elif:
    ação

Laços de Repetição:

while(condição):
    ação
'''

idade = 20
if (idade >= 18):
    print("Maior de idade")
else:
    print("Menor de idade")

print("########################################")

nota1 = 5.6
nota2 = 4.7
nota3 = 8.8
media = (nota1+nota2+nota3)/3
presenca = 98 #porcentagem


print("Média:",media)
print("Presença:",presenca,"%")
if (media >= 7) and (presenca >= 70):
    print("Aprovado")
elif(media >= 5):
    print("Recuperação")
else:
    print("Reprovado")

print("########################################")

numero_sorteado = 15
numero_escolhido = int(input("Escolha um numero entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou, escolha outro numero")
    numero_escolhido = int(input("Escolha um numero entre 1 e 20: "))
print("Você Acertou !")