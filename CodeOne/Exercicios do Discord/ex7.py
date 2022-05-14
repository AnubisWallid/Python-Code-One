'''
Questão 7.
Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
euclidiana entre os pontos, utilizando a equação abaixo:
𝑑 = V((𝑥2 − 𝑥1)² + (𝑦2 − 𝑦1)²)

'''

import math

x_1 = float(input("Coodernada do ponto X 1: "))
y_1 = float(input("Coodernada do ponto Y 1: "))
x_2 = float(input("Coodernada do ponto X 2: "))
y_2 = float(input("Coodernada do ponto Y 1: "))

calculo_distancia = math.sqrt(((x_2 - x_1)**2)+((y_2 - y_1)**2))

print(f"A distancia entre o ponto ({x_1},{y_1}) e ponto ({x_2},{y_2}) é = {calculo_distancia}")