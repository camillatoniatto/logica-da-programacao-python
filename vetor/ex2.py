#Ler 8 elementos em uma matriz A tipo vetor. 
#Construir uma matriz B de mesma  dimensão com os elementos da matriz multiplicados por 5. 
#Apresentar a matriz B  na ordem crescente.

A=[] 
B=[] 
for i in range (8): 
    numb=int(input("Digite valor: ")) 
    A.append(numb) 
for i in range (8): 
    B.append(A[i]*5) 
B.sort() 
for i in B: 
    print(i)
