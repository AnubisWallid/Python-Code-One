'''
Questão 8.
Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
Dica: Use três variáveis:
● um contador;
● uma variável para soma;
● e uma variável para os termos.
Lembre-se de que 4! = 4 * *3 ** 2 * *1, que também é igual a 4 ** 3!

'''
soma = 0
count = 1
var = 1
while count <= 1000:
    var = var / count
    soma += var
    count += 1
    # print(var)
print(soma)