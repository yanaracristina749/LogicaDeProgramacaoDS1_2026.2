"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_consumido = input("qual o valor consumido no restaurante em R$?")
resultado = (float(total_consumido)/100)*10
resultado2 = float(resultado)+float(total_consumido)
print(f"o valor da conta deu {resultado2:.2f}R$")