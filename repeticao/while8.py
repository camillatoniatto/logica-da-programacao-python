#Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo. 
#A série de Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34...etc. 
#Esta série se caracteriza pela soma de um termo posterior com o seu anterior subsequente
anterior = 0
proximo = 1
while proximo<700:
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior
