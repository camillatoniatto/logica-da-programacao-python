#Ler duas matrizes do tipo vetor A com 20 elementos e B com 30 elementos.  
#Construir uma matriz C, sendo esta a junção das duas outras matrizes. 
#Desta  forma, C deverá ter a capacidade de armazenar 50 elementos. 
#Apresentar os  elementos da matriz C em ordem decrescente.
A=[] 
B=[] 
C=[] 
for i in range (2): 
    numb=int(input("Digite valor para vetor A: ")) 
    A.append(numb) 
for i in range (3): 
    numb=int(input("Digite valor para vetor B: ")) 
    B.append(numb) 
for i in A: 
    C.append(i) 
for i in B: 
    C.append(i) 
C.sort() 
for i in reversed(C): 
    print(i)
