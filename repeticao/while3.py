'''
Apresentar os resultados de uma tabuada de um número qualquer. Esta deverá ser impressa no seguinte formato:
Considerando como exemplo o fornecimento do número 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
....
2 x 9 = 18
2 x 10 = 20
'''
numero=int(input("Insira um numero para a tabuada: "))
i=0
while i<10:
	i = i + 1
	resultado = numero * i
	print(numero,'*',i,'=',resultado)	