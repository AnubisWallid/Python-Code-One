'''
Questão 2.
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos.

'''
numero = float(input("ïnforme um numero de 0 a 100: "))

if numero >= 0 and numero <= 25:
    print("0 <-> 25")
elif numero > 25 and numero <= 50:
    print("25 <-> 50")
elif numero > 50 and numero <= 75:
    print("50 <-> 75")
elif numero > 75 and numero <= 100:
    print("75 <-> 100")
else:
    print("Numero fora do intervalo")
