'''
Questão 4.
Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.
'''

numero_int_1=int(input("Digite o primeiro numero, inteiro: "))
numero_int_2=int(input("Digite o segundo numero, inteiro: "))
numero_real=float(input("Digite o terceiro numero, real: "))
a = (numero_int_1 * 2) * (numero_int_2 / 2)
b = (numero_int_1 * 3) + numero_real
c = numero_real ** 3

print("a) : ",a)
print("b) : ",b)
print("c) : ",c)