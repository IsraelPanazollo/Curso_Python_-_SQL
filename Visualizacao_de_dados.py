#Visualização de dados em Python

#1 Gráfico de linhas

import matplotlib.pyplot as plt

x = [1,2]
y = [2,3]

plt.title("Meu primeiro gráfico em Python")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x,y)
plt.show()

#2 Gráfico de barras

x = [1,2,3,4,5]
y = [2,3,7,0,1]

plt.title("Gráfico de barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x,y)
plt.show()

#3 Comparação em gráfico de barras

x1 = [1,3,5,7,9]
y1 = [2,3,7,0,1]
x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

plt.title("Gráfico de barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.legend()
plt.show()

#4 Gráfico de dispersão

x = [1,2,3,4,5]
y = [2,3,7,0,1]

plt.title("Gráfico de dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.scatter(x,y)
plt.show()

# Para salvar figuras

x = [1,2,3,4,5]
y = [2,3,7,0,1]
z = [200, 25, 400, 3000, 100]

plt.title("Gráfico de dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x,y, color = "#000000", linestyle = "--")
plt.scatter(x,y, label = "Meus Pontos", color = "k", marker = ".", s=z)
plt.legend()
plt.show()

plt.savefig("figura1.png")