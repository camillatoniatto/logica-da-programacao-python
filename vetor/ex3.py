#Ler a matriz A do tipo vetor com 15 elementos. 
#Construir uma matriz B de mesmo  tipo, sendo que cada elemento da matriz B seja a fatorial do elemento correspondente da matriz A. 
#Apresentar os elementos da matriz B ordenados de  forma crescente

A=[] 
B=[] 
for i in range (15): 
    numb=int(input("Digite valor: ")) 
    A.append(numb) 
    fatorial=1 
    for i in range(1,numb+1): 
        fatorial *= i 
    B.append(fatorial) 
B.sort() 
print(B)
