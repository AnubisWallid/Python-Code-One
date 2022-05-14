##### Funções
'''
### Função Inicial # Define

from random import random


def saudacao(nome = "senhor(a)"):
    print("Ola como vai,",nome)
### Com parametros e default
saudacao("Forasteiro")
saudacao()

### Função com retorno

def getOlaMundo():
    return "Olá, Mundo"

print(getOlaMundo())

print(random()*100)
print(random()*100)
print(random()*100)
print(random()*100)
'''
### testes aleatorios

def standard_arg(arg):
     print(arg)
def pos_only_arg(arg, /):
     print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
standard_arg(arg=1)
standard_arg(1)
# pos_only_arg(arg=2)
pos_only_arg(2)
# kwd_only_arg(3)
kwd_only_arg(arg=3)
combined_example(1,2,kwd_only=3)