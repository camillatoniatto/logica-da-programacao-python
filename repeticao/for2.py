#Apresentar o total da soma obtido de N números inteiros

numb=int(input("Digite um numero inteiro: "))
vezes=int(input("Digite quantas vezes irá multiplicar: "))
i=1
soma=0
for i in vezes:
	i = i+ 1
	soma += numb
	print("Valor da soma dos números: ",soma )
