"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
A = float(input("Digite o valor do coeficiente A: "))
B = float(input("Digite o valor do coeficiente B: "))
C = float(input("Digite o valor do coeficiente C: "))
if A == 0:
    print("Impossível calcular")
elif (B ** 2 - 4 * A * C) < 0:
    print("Impossível calcular")
else:
    delta = (B ** 2) - (4 * A * C)
    R1 = (-B + delta ** 0.5) / (2 * A)
    R2 = (-B - delta ** 0.5) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
