#Ler duas matrizes A e B, cada uma de duas dimensões com 5 linhas e 3 colunas.
#Construir uma matriz C de mesma dimensão, onde C é formada pela soma dos
#elementos da matriz A com os elementos da matriz B
A = []
B = []
C = []
for i in range (5):
    x=[]
    for j in range (3):
        x.append(int(input("Digite valor matriz A: ")))
    A.append(x)
for i in range (5):
    x=[]
    for j in range (3):
        x.append(int(input("Digite valor matriz B: ")))
    B.append(x)
for i in range (5):
    x=[]
    for j in range (3):
        x = A[i][j]+B[i][j]
    C.append(x)
print(C)