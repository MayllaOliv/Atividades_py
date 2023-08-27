alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

print("Dicionário de alunos:", alunos)

alunos = {}
soma_notas = 0

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota
    soma_notas += nota

media = soma_notas / len(alunos)
print("Média das notas:", media)

