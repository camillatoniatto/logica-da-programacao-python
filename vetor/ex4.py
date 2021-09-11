#Ler uma matriz A com 12 elementos. Após a sua leitura, colocar os seus elementos  em ordem crescente. 
#Depois ler uma matriz B também com 12 elementos. Colocar  os elementos de B em ordem crescente. 
#Construir uma matriz C, onde cada  elemento de C é a soma do elemento correspondente de A com B. 
#Colocar em  ordem crescente a matriz C e apresentar os seus valores

A=[] 
B=[] 
C=[] 
for i in range (12): 
    numb=int(input("Digite valor para vetor A: ")) 
    A.append(numb) 
    A.sort() 
for i in range (12): 
    numb=int(input("Digite valor para vetor B: ")) 
    B.append(numb) 
    B.sort() 
for i in range (12): 
    C.append(A[i]+B[i]) 
    C.sort() 
print(C)
