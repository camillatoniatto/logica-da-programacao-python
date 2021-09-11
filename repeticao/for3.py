#Apresentar o fatorial de N números inteiros
numb=int(input("Numero para calcular o fatorial: "))
fatorial=1
for x in range(1,numb+1):
    fatorial *= x
print("O fatorial de",numb,"! é:",fatorial)
