#Apresente todos os valores numéricos inteiros ímpares situados na faixa de 1000 a 1500
numb = 1000
for numb in range (1000,1500):
	numb = numb + 1
	if numb%2!=0:
		print(numb)