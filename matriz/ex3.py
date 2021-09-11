#Ler 20 elementos para uma matriz qualquer, considerando que esta matriz tenha
#o tamanho de 4 linhas por 5 colunas
A= []
for i in range (4):
    x=[]
    for j in range (5):
        x.append(int(input("Digite valor matriz A: ")))
    A.append(x)
for i in A:
    print(i)