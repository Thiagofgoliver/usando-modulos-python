#faça um programa que leia o nome de quatro alunos e coloque em ordem que ira apresentar primeiro .
from random import shuffle
n1 = str (input ('escreva o nome do aluno 1'))
n2 = str (input ('escreva o nome do aluno 2'))
n3 = str (input ('escreva o nome do aluno 3'))
n4 = str (input ('escreva o nome do aluno 4'))

lista = [n1,n2,n3,n4]
shuffle (lista)
print ('a ordem da lista será ')
print (lista)