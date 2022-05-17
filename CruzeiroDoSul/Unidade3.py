##### Conteudo: While e For

### While

qtdvalores = int(input("Digite a quantidade de números que serão calculados "))
count= 0
valor = 0

while count < qtdvalores:
    valor += float(input("Digite um valor "))
    count+=1

media = valor / count

print(media)

#### For

qtdvalores = int(input("Digite a quantidade de números que serão calculados "))

valor = 0

for i in range(qtdvalores):
    valor += float(input("Digite um valor "))
    i+=1

media = valor / i 

# Interessante que diferente de outras linguagens,
# a variavel "i" pode ser usada fora do laço

print(media)