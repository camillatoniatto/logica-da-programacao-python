#Apresentar os resultados de uma tabuada de um número qualquer
numero=int(input("Insira um numero para a tabuada: "))
i=0
for i in range (10):
	i = i + 1
	resultado = numero * i
	print(numero,'*',i,'=',resultado)
