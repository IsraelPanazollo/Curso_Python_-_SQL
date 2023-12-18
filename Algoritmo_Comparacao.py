lista=[]

print("Digite quantos números: ")
k=int(input())

print("Digite os números para comparação: ")
for i in range(k):
    aux=float(input())
    lista.append(aux)

print("Está é a sua lista: ")
print(lista)

for i in range(k):
    menor=i
    for j in range(i+1,k):
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print("Esta é a lista ordenada: ")
print(lista)
