#Apresentar todos os números divisíveis por 5 que sejam menores que 15
numb = 1
for numb in range (15):
	numb = numb + 1
	if numb%5==0:
		print(numb)
