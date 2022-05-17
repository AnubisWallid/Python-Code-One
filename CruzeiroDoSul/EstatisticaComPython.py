from gettext import find
import random


qtd_variaveis = 20 #int(input("Quantas variaveis serão geradas? > "))
faixa_valoresMin = 0 #int(input("Qual a faixa de valores? Menor valor > "))
faixa_valoresMax = 10 #int(input("Qual a faixa de valores? Maior valor > "))


lista_var = []

faixa_1 = []
faixa_2 = []
faixa_3 = []
faixa_4 = []
faixa_5 = []


for i in range(qtd_variaveis+1):
    lista_var.insert( i, round( random.uniform( faixa_valoresMin , faixa_valoresMax ) ,1) )
    # print(lista_var[i])
    if lista_var[i] >= 0 and lista_var[i] <= 3.9:
        faixa_1.insert(i,lista_var[i])
    elif lista_var[i] >= 4 and lista_var[i] <= 5.9:
        faixa_2.insert(i,lista_var[i])
    elif lista_var[i] >= 6 and lista_var[i] <= 7.9:
        faixa_3.insert(i,lista_var[i])
    else:
        faixa_4.insert(i,lista_var[i])

lista_var.sort()

print(lista_var,'\n')
print(f'|{"Faixa das notas":^21}|{"Frequência":^21}|{"Relativa":^21}|{"Porcentagem":^21}|')
print(f'|{"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -":^87}|')
print(f'|{"Notas de 0 - 4":^21}|{len(faixa_1):^21}|{(len(faixa_1)/qtd_variaveis):^21}|{(len(faixa_1)/qtd_variaveis)*100:^21}|')
print(f'|{"Notas de 4 - 6":^21}|{len(faixa_2):^21}|{(len(faixa_2)/qtd_variaveis):^21}|{(len(faixa_2)/qtd_variaveis)*100:^21}|')
print(f'|{"Notas de 6 - 8":^21}|{len(faixa_3):^21}|{(len(faixa_3)/qtd_variaveis):^21}|{(len(faixa_3)/qtd_variaveis)*100:^21}|')
print(f'|{"Notas de 8 - 10":^21}|{len(faixa_4):^21}|{(len(faixa_4)/qtd_variaveis):^21}|{(len(faixa_4)/qtd_variaveis)*100:^21}|')