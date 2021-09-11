#Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500
numb = 1
soma=0
while numb<500:
	numb = numb + 1
	if numb%2==0:
		soma += numb
		print(numb,"+ termo anterior = ",soma )