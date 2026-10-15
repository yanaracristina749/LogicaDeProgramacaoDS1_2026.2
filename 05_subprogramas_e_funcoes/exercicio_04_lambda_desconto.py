"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
desconto = lambda valor: valor * 0.85

valor_produto = 100
valor_desconto = desconto(valor_produto)

print("Valor original: R$", valor_produto)
print("Valor com desconto: R$", valor_desconto)