'''
Questão 3.
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
'''

import math

raio_circulo = float(input("Informe o raio do circulo: "))

area_circulo = math.pi * raio_circulo ** 2
print(f"A area do circulo, de raio: {raio_circulo}, é igual a: {area_circulo}")