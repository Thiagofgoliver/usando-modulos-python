# aprender usar modulos no py 
# comandos import e from / import 
#     o python assim  como java e varias outras linguagens ela é uma linguagem que trabalha a partir de pacotes,
#     a partir de modulos instaveis e modulos já pré definidos ,mais quando voce cria um programa em python ele...
#...vem com o basico.

#                                        exemplos 

# o corpo humano como se fosse uma maquina mais conforme vai passando o tempos vamos ficando fracos , e assim precisamos
# de uma adição , adicionar algumas coisas ,  a  gente adiciona comida , bebida , doçe esses recursos não são padronizados ...
# ... mais a gente precisa adicionar esses modulos para fazer algumas funcionabilidades durante o dia .
#  tenho uma mesa cheia de alimentos e esses alimentos e esses alimentos são doçe salgados e sucos , cada um chamarei de bibliotecas de comidas .[
# pois posso colocar esses alimentos a qualquer momento em meu corpo  para que ele possa fazer as funcionabilidades a que ele se presta
# 
#no linguajar da programação a gente pode fazer importações nesse tipo de biblioteca , os programas em python tem 
# um certo tipo de limitação nos comandos isso funciona para que a linguagem seja rapida e que os programas seje pequenos
# e não consuma memoria e dé gastos adicionais sem necessidades sé for preciso traga de fora e importo para meu programa
# ai esses recursos passam a funcionar .
#
#                       import
# dentro da linguagem python para eu importar algo eu ultilizo o import .
# exemplo 
#   import bebida todas as bebidas da mesa serão importadas 
#   import comida todas as comidas da mesa serão importadas
#   import doçe todos os doçes da mesa sera importados
#   então basicamento no python voçe irá dar o comando import nas primeiras linhas inports necessarios para esse programa 
# e irá colocar o nome do modulo e da biblioteca que vai ser carregadas para esse programa.
#  só que ai voce para pensar quando voce da inport doçes e irá vir todos os doçes e se quiser só um pudim ,vou ter que
# por todos doçes na mesa e não vou comer tudo ? 
# para fazer inportações unicas o comando será !
#
#               from import doçe "pudim " importa o doçe selecionado 
#                          X
#               import doçe  importa todos doçes da biblioteca 
#                           
#                 BIBLIOTECA PADRAO  matematica "math" 
#  Bibloteca muito especifica assim que voce baixa o python ela já vem incluida só não vem importada nos programas 
#  para traser algumas funcionalidades matematicas extras.
#  exemplos quero tirar a media de um aluno ele tirou 7,25 e se caso eu quiser aredondar um pouco para cima 
# ai voce tera que importar a biblioteca math  e ultilizar a funcionalidade ceil "ceil" irá fazer um arredondamento para cima
# de maneira similar temos a funcionalidade floor que faz um arredondamento para baixo ,
# temos a funcionabilidade trunc ele elimina a ',' para frente sem fazer arredondamento nenhum simplesmente vai truncar.
# temos a funcionalidade pow "power " potencia  que funciona parecido com os ** 
# temos a funcionalidade sqrt para calcular raiz quadrada 
#  temos a funcionalidade factorial para calculo de fatorial .
#
#   " import math"" ele irá importar essas funcionalidades a cima e muitas outras.

# e se caso quiser usar só a raiz quadrada 
#      
#  " from msth import sqrt " ira traser só a funcionalidade sqrt 

# caso queira usar duas funcionalidades para importar uso ,
# 
#" from msth import sqrt , pow" só colocar virgula e escrever a funcionalidade necessaria

# colocando em platica

# quero calcular a raiz desse numero
import math 
num = int (input('escreva um numero : '))
raiz = math.sqrt (num)
print ( ' a raiz de {:.2F} é igual a {:.2F}  ' .format (num,raiz))

# TRASENDO  A NECESSARIA 
from math import sqrt
num = int (input('escreva um numero : '))
raiz = sqrt (num)
print ( ' a raiz de {} é igual a {:.2F}  ' .format (num,raiz))

# TRASENDO  duas 
from math import sqrt,floor 
num = int (input('escreva um numero : '))
raiz = sqrt (num)
print ( ' a raiz de {} é igual a {:.2F}  ' .format (num,floor(raiz))) 

#como visualizo as bibliotecas que quero importar vai no site oficial do python clica em docs e visualiza em sua ide a versao do python
#e no site coloca a versao mais proxima da versao da ide , clica em library referencies se voce for no capitulo 9 mostrara todas referencias e funcionalidades para dar estudada!
#exemplo biblioteca para numeros aleatorios "random"
#print (num)
# a funcionalidade vai muito alem , voltando no python.worg clique em pypi 'py'de python e 'pi'indice de pacotes extras 
# clicando em browse packages  ele mostras varias  opçoes de biblioteca 
 
 # como usar biblioteca de emoji no prompt de comando do seu windows digite o comando pip install emoji  ira instalar a biblioteca

#import emoji
#print (emoji.emojize("olá , mundo:sunglasses:",use_aliases=True))
