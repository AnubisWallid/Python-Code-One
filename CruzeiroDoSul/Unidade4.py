##### List, Dictionary e Tuple

### Lista: sequência ordenada de elementos e mutável // List em Java

lista_nomes = ['joao','maria','jose','tadeu','ricardo']
lista_nomes[0] = 'joão'
lista_nomes.pop()
lista_nomes.append('ricardo2')

try:
    lista_nomes.remove("maria")
    print(lista_nomes)
except:
    print("O valor não existe na lista")

print(lista_nomes)

### Tuplas: Sequência ordenada de elementos imutáveis e não pode ser atualizado // Set em Java

tupla_numeros = (11,12,13,14,15,16,17)
print(tupla_numeros[4])

#adicionando mais um numero
del tupla_numeros
tupla_numeros = (10,11,12,13,14,15,16,17)
print(tupla_numeros)

### Dicionarios: Sequência de elementos com chaves e valores // Map em Java

dict_relatorio = {
    "nome":"",
    "idade":""
}

relacao = []
dict_relatorio['nome']='joao'
relacao[0] = dict_relatorio
dict_relatorio['nome']='maria'
relacao[1] = dict_relatorio

print(relacao)
a = 1
b = 2
if (a == 0):
    print(a)
else:
    if(b == 2):
        print(b)
