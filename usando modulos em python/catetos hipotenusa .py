'''crie um programa que leia o comprimento do cateto oposto e do cateto adjecente de um triangulo retangulo
calcule e mostre o comprimento da hipotenusa.'''

''' sem import 
co = float (input ('comprimento do cateto oposto :'))
ca = float (input ('comprimento do cateto adjecente : '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('a hipotenusa vai medir {:.f} '.format (hi))'''

# com import 
from math import hypot
co = float (input ('comprimento do cateto oposto :'))
ca = float (input ('comprimento do cateto adjecente : '))
hi = hypot(co,ca)
print ('a hipotenusa vai medir {:.2f}'.format (hi))
