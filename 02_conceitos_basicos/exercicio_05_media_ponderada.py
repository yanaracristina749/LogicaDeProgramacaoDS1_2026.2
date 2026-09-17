"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input ("qual a sua primeira nota da avaliação?"))
nota2 = float(input ("qual a sua segunda nota da avaliação?"))
nota3 = float(input ("qual a sua terceita nota da avaliação?"))
resultado1 = (nota1*2)+(nota2*3)+(nota3*5)
resultado2 = resultado1/10
print(f"a média é :{resultado2:.2f}")
