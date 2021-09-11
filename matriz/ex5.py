#Ler duas matrizes A e B, cada uma com uma dimensão para 12 elementos.
#Construir uma matriz C de duas dimensões, onde a primeira coluna da matriz C
#deverá ser formada pelos elementos da matriz A multiplicados por 2, e a segunda
#coluna deverá ser formada pelos elementos da matriz B subtraídos de 5.
A=[]
B=[]
C=[]
print("Matriz A")
for i in range (12):
    A.append(int(input("Digite valor: ")))
print("Matriz B")
for i in range (12):
    B.append(int(input("Digite valor: ")))
print("Matriz C")
for i in range (12):
    x=[]
    x.append(A[i]*2)
    x.append(B[i]-5)
    C.append(x)
for i in C:
    print(i)