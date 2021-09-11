# Ler 12 elementos de uma matriz tipo vetor, colocá-los em ordem decrescente e  apresentar os elementos ordenados 
A=[] 
B=[] 
for i in range (12): 
    numb=int(input("Digite valor: ")) 
    A.append(numb) 
A.sort() 
for i in A[::-1]:  
    print(i)
