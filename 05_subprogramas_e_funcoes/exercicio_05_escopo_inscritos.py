"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_inscritos = 0
def inscrever_aluno(quantidade):
    global total_inscritos
    total_inscritos = quantidade
    return total_inscritos
quantidade = int(input ("Digite a quantidade de alunos inscritos:"))
print("Antes da chamada:", total_inscritos)
print("Depois da chamada:", inscrever_aluno(quantidade))