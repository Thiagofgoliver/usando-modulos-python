#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno , cosseno e tangente desse angulo.
from math import radians,sin,cos,tan
angulo = float (input ('digite o angulo que voce deseja :'))
seno = radians (angulo)
print ('o angulo de {} tem o seno de {:.2f}'.format (angulo , seno))

cosseno = cos (radians (angulo))
print ('o angulo de {} tem o cosseno de {:.2f}'.format (angulo, cosseno ))

tangente = tan (radians(angulo))
print ('o angulo de {} tem a tangente de {:.2f}'.format(angulo,tangente))  