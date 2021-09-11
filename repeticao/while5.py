#Apresentar todos os números divisíveis por 4 que sejam menores que 200. Para verificar se o número é divisível por 4,
#efetuar dentro da malha a verificação lógica desta condição com a instrução se,
#perguntando se o número é divisível; sendo, mostre-o; não sendo, passe para o próximo passo.
#A variável que controlará o contador deverá ser iniciada com valor 1
numb = 1
while numb<200:
	numb = numb + 1
	if numb%4==0:
		print(numb)
		
else:
      print("O loop while foi encerrado com sucesso!")
