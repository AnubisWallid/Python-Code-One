'''
Questão 10.
Na música, uma nota tem um tom (sua frequência, resultando em quão grave ou agudo é o
som) e uma duração (por quanto tempo a nota soa). Neste problema, estamos interessados
apenas na duração das notas.
Marcos está dando os primeiros passos para ser um compositor de jingles. Ele está tendo alguns
problemas, mas ao menos ele está criando melodias agradáveis e ritmos atrativos. Um jingle é
dividido em uma sequência de compassos, e um compasso é formado de uma série de notas.
A duração de uma nota é indicada pela sua forma. Neste problema, iremos utilizar letras
maiúsculas para indicar a duração de uma nota. A seguinte tabela lista todas as notas
disponíveis:

NOTAS   |  o  |  o| |  .| | .|  |  .|" | .|"' | .|"" |
ID      |  W  |  H  |  Q  |  E  |   S  |   T  |   X  |
DURAÇÃO |  1  | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 |

A duração de um compasso é a soma da duração de suas notas. Nos jingles de Marcos, cada
compasso tem a mesma duração. Como Marcos é apenas um iniciante, seu famoso professor
Johann Sebastian III o ensinou que a duração de um compasso deve ser sempre 1.
Por exemplo, Marcos escreveu uma composição contendo cinco compassos, dentre os quais
quatro possuem a duração correta e um está errado. No exemplo abaixo, cada compasso é
delimitado com barras e cada nota é representada como na tabela acima.

'''
# compasso = input("Entre com o compasso: ")
tempo_nota = {
  'W': 1,
  'H': 1/2,
  'Q': 1/4,
  'E': 1/8,
  'S': 1/16,
  'T': 1/32,
  'X': 1/64
}

# compasso = "/HH/QQQQ/XXXTXTEQH/W/HW/"
compasso = "/W/W/SQHES/HH/QQQQ/WE/TEX/THES/"

compasso = compasso.strip('/')
compasso = compasso.split('/')
# print(compasso)
corretos = 0
incorretos = []

for i in compasso:
  tempo_compasso = 0
  for id in i:
    tempo_compasso += tempo_nota[id]
  
  if tempo_compasso == 1:
    corretos += 1
  else:
    incorretos.append(i)

print('Corretos:', corretos)
if len(incorretos) > 0:
  print('Incorretos:', incorretos)