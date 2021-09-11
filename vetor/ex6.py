#Ler 30 elementos de uma matriz A do tipo vetor. 
#Construir uma matriz B de mesmo  tipo, observando a seguinte lei de formação: 
#Todo elemento de B deverá ser o  cubo do elemento de A correspondente.
A=[] 
B=[] 
for i in range (30): 
    numb=int(input("Digite valor: ")) 
    A.append(numb) 
for i in A: 
    B.append(i**3) 
print(B)
