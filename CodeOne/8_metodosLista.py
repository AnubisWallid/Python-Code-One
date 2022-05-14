##### Métodos e Funções de Listas
lista = [1,25,25,33,25,0,25,45]

### append() > adiciona um elemento no final da lista
lista.append(500)
print("Lista depois do append",lista)

### insert() > adicionar um elemento escolhendo o indice da lista
lista.insert(1,77)
print("Lista depois do insert",lista)

### extend() > Junta duas listas
lista2 = [0,1,2,3]
lista.extend(lista2)
print("Lista depois do extend",lista)

### pop() > Remove o ultimo elemento caso nao especifique o indice
lista.pop()
print("Lista depois do pop",lista)

### remove() > Remove o elemento pelo valor dele, o primeiro que encontrar
lista.remove(25)
print("Lista depois do remove",lista)

### count() > conta quantas vezes um elemento aparece
print(f"O numero 25 aparece: {lista.count(25)} vezes")

### index() > Diz o indece do elemento
print("Posição do número 33: ",lista.index(33))

### sort() > Organiza a lista
lista.sort()
print("Lista depois do sort",lista)
lista.sort(reverse=True)
print("Lista depois do sort(reverse=True)",lista)

### reverse() > Reverte a lista
lista.reverse()
print("Lista depois do reverse",lista)

##### Funções para Lista

# len
print(len(lista))
# sum
print(sum(lista))
# max
print(max(lista))
# min
print(min(lista))


