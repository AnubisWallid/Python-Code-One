##### Listas = Array em JS

### Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

### Com lista
notas = [7.9,9.7,8.2]

### Criando Listas
lista = [] # Lista vazia
lista = list() # Lista vazia
lista = [1,"Wallid",True,12.55,"ultimo item da lista"] # Recebe vários tipos de dados
multidimencional = [lista,[10,11,12]] # pode receber outra lista

### Indexação e Slices(Fatiamento)
print(multidimencional[0][0])
print(multidimencional[0][1])
print(multidimencional[0][2])
print(multidimencional[0][3])
print(multidimencional[1][0])
print(multidimencional[1][1])
print(multidimencional[1][2])
print(multidimencional[0][-1])

### Slices
lista2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lista2[0:3])
print(lista2[3:]) # vai até o final
print(lista2[0::2]) # terceiro parametro pula de 2 em 2

### Interação com FOR
for i in multidimencional: # Igual ao for each no JAVA
    for j in i:
        print(j)

### Utilizando os indices
print(len(multidimencional[0])) # 5
print(len(multidimencional[1])) # 3