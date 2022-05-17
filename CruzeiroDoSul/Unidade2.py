##### Precedência de Operações
'''
1º Parênteses ()
2º Inversão de sinal -
3º Exponenciação **
4º Multiplicação, Divisão, Resto da divisão (módulo) *, /, %, //
3º Adição e Subtração +, -

Em uma expressão com operadores da mesma prioridade, 
    as operações serão executadas da esquerda para a direita.
'''

### Operador lógico AND para comparar duas expressões lógicas
a=5
b=5
c=2
d=1
if(a==b) and (c>d):
    print("A primeira e a segunda expressão retornam 'verdadeiro'")
    

### Operador lógico OR para comparar duas expressões lógicas
a=5
b=2
c=2
d=1
if(a==b) or (c>d):
    print("A primeira expressão retornam 'falso', porém a segunda expressão retorna 'verdadeiro'")
    
    
### Operador lógico NOT para comparar duas expressões lógicas
a=5
b=5
if not(a!=b):
    print("A expressão retorna 'falso', porém o operador NOT inverte o resultado")