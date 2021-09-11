#Elaborar um programa que apresente o valor de uma potência de uma base qualquer elevada a um expoente qualquer, ou seja, de NM

numb=int(input("Digite um numero inteiro: "))
m=int(input("Digite outro numero inteiro: "))
potencia=1
i=0
while i<m:
	potencia = potencia*numb
	i = i+1
	print(numb,'^',i,'=',potencia)	