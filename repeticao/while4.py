#Ler um número N qualquer menor ou igual a 50 e apresentar o valor obtido da multiplicação 
#sucessiva de N por 3 enquanto o produto for menor que 250 (N*3, N*3*3, N*3*3*3; etc)
numero=int(input("Insira um numero menor ou igual 50: "))
i=3
while numero<=50:
	produto = numero * i
	i = i * 3
	if produto<=250:
		print(produto)
else:
	print("O número inserido foi maior que 50")
