#Estudo de caso população brasileira

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População em 100 milhões")

plt.bar(x,y,color="#e4e4e4")
plt.plot(x,y,color="k",linestyle="--")
#plt.scatter(x,y,color="r")
plt.show()
plt.savefig("populacao_brasileira.png", dpi=300)