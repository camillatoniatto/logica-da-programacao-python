#Ler 20 elementos de uma matriz A tipo vetor e construir uma matriz B da mesma  dimensão com os 
#mesmos elementos de A acrescentados de mais 2. Colocar os  elementos da matriz B em ordem crescente.
A=[] 
B=[] 
for i in range (20): 
    numb=int(input("Digite valor: ")) 
    A.append(numb) 
for i in A: 
    B.append(i+2) 
B.sort() 
print(B)
