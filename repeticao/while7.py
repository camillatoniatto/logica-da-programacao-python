'''
Apresentar as potências de 3 variando de 0 a 15. Deve ser considerado que qualquer número elevado a zero é 1, e elevado a 1 é ele próprio.
Deverá ser apresentado, observando a seguinte definição:
30 = 1
31 = 3
32 = 9
...
315 = 14348907
'''
numero=int(input("Insira um numero: "))
i=-1
while i<15:
	i = i + 1
	resultado = numero**i
	print(numero,'^',i,'=',resultado)	
