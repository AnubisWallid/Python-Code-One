##### Laço de Repetição FOR
'''
for variavel in range(10):
    ação
'''
for i in range(1,11):# Um parametro: 0 a 10
    print(i)

print("########################################")

for i in range(1,11):# Dois parametros: 1 a 10 paramentros 
    print(i)

print("########################################")

for i in range(1,11,2):# Tres parametros: 1 a 10 pulando 2 em 2
    print(i)
print("########################################")

qtd = int(input("Informe a quantidade de notas que serão computadas: "))
soma = 0
for i in range(qtd):
    nota = float(input(f"Nota {i+1}: "))
    soma += nota
media = soma / qtd
print("A media das notas foi:",media)