#crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira.

#ex: digite um numero :6.127
# o numero 6.127 tem a parte inteira 6.
 

 #importando biblioteca 
'''from math  import trunc
num = float (input ('digite um valor :'))
print ( ' o valor digitado foi {} sua porção inteira é {}'.format (num, trunc(num)))'''

#sem importar 
num = float (input ('digite um valor: '))
print ("o valor digitado foi  {} e a porção inteira é {} ". format (num , int (num)))
