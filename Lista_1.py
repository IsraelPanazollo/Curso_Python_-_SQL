# Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.

print("Digite sua idade: ")
idade=int(input())

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

print("Digite suas duas notas: ")
nota_1=float(input())
nota_2=float(input())

if nota_1 >=6 and nota_2 >= 6:
    print("Aprovado")
else:
    print("Reprovado")

# Escreva um programa que resolva uma equação de segundo grau.

from math import sqrt

print("Com a equação na forma A.x^2+B.x+C=0, digite A, B e C")

a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c
raiz_delta = sqrt(delta)

if raiz_delta < 0:
    print("Solução fora dos números reais")
else:
    x1 = (-b + raiz_delta) / 2 * a
    x2 = (-b - raiz_delta) / 2 * a

    print("As raízes são", x1, "e", x2)

# Escreva um programa que ordene uma lista numérica com três elementos.

print("Digite 3 números: ")
a=float(input())
b=float(input())
c=float(input())

lista = [a,b,c]
lista_ordenada = sorted(lista)

print(lista_ordenada)

# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

print("Digite 2 números: ")
a=float(input())
b=float(input())

print("Digite a operação: ")
operacao=input()

print("Resultado:")
if operacao == "+":
    print(a+b)
elif operacao == "-":
    print(a-b)
elif operacao == "*":
    print(a*b)
elif operacao == "/" and b!=0:
    print(a/b)
else:
    print("Operação inválida")
