#### Dicionários > Iguais aos Objetos Literais em JavaScript

### Criar Dicionario
dic = {}
dic = dict()
dic = {"nome":"Wallid",
    "idade":28,
    "altura": 1.79}

print(f"Nome {dic['nome']}, Idade {dic['idade']}, Altura {dic['altura']}")

### Adicionar uma nova chave

dic["Dev"] = True
print(dic)

### Interando

for i in dic:
    print(i,dic[i])

### Testando a existencia de uma Chave

print("peso" in dic)