#Ler duas matrizes A e B, cada uma com uma dimensão para 7 elementos. Construir
#uma matriz C de duas dimensões, onde a primeira coluna deverá ser formada pelos
#elementos da matriz A e a segunda coluna deverá ser formada pelos elementos da
#matriz B
A= []
B= []
C= []
print("Matriz A")
for i in range (7):
    A.append(int(input("Digite valor: ")))
print("Matriz B")
for i in range (7):
    B.append(int(input("Digite valor: ")))
print("Matriz C")
for i in range (7):
    x=[]
    x.append(A[i])
    x.append(B[i])
    C.append(x)
for i in C:
    print(i)