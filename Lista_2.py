#Escreva um programa que compare se duas sequências digitadas pelo usuário são iguais.

S_1=input("Digite uma sequência: ")
S_2=input("Digite outra sequência: ")

if S_1==S_2:
    print("As sequências são iguais")
else:
    print("As sequências são diferentes")


#Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.
nome= input("Digite o nome do arquivo com sua extensão:")

arquivo = open(nome)

leitura = arquivo.read()

print(leitura)

#Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato fasta.

seq= input("Digite uma sequência:")

arquivo = open("Seq_digitada.fasta","w")

arquivo.write(seq)

#Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer. Se o usuário digitar 1, o programa deve chamar uma função que lê um arquivo de texto. Se o usuário apertar 2, o programa deve imprimir o conteúdo do arquivo lido anteriormente. Se o usuário apertar três o programa deve ser fechado.
print("Menu de opções \nDigite 1 para ler um arquivo de texto \nDigite 2 para visualizar o conteúdo do arquivo de texto lido anteriormente \nDigite 3 para encerrar o programa")
opcao = 0

while opcao != 3:
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        nome = input("Digite o nome do arquivo:")
        arquivo = open(nome)
        print("O arquivo foi aberto")
    if opcao == 2:
        try:
            leitura = arquivo.read()
            print(leitura)
        except NameError:
            print("Não foi selecionado um texto anteriormente")

#Escreva um programa que leia um arquivo multi-fasta e armazene em um dicionário: cabeçalho da sequência como a chave e a sequência como valor.

arquivo = open("Sequencias.txt")

linhas = arquivo.readlines()

dicio = {}

for linha in linhas:
    if linha[0] == ">":
        seq_atual = linha[1:].strip()
    else:
        try:
            dicio[seq_atual] = linha.strip()
        except:
            pass
print(dicio)