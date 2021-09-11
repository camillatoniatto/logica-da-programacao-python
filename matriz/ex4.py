#Ler uma matriz A de uma dimensão com 10 elementos. Construir uma matriz C de
#duas dimensões com três colunas, onde a primeira coluna da matriz C é formada
#pelos elementos da matriz A somados com mais 5, e a segunda coluna é formada
#pelo valor do cálculo do fatorial de cada elemento correspondente da matriz A e a
#terceira e última coluna deverá ser formada pelos quadrados dos elementos
#correspondente da matriz A.
A=[]
C=[]
for i in range (10):
    x=int(input("Digite valor matriz A: "))
    A.append(x)
for i in A:
    x=[]
    x.append(i+5)
    fatorial=1
    for i in range(1,i+1):
        fatorial *= i
    x.append(fatorial)
    x.append(i**2)
    C.append(x)
for i in C:
    print(i)