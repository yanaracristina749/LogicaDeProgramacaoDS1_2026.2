"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo_item = int(input("Digite o código do item (1 a 5):"))
quantidade = int(input("Digite a quantidade consumida:"))
match codigo_item:
    case 1:
        total = quantidade * 4.00
    case 2:
        total = quantidade * 4.50
    case 3:
        total = quantidade * 5.00
    case 4:
        total = quantidade * 2.00
    case 5:
        total = quantidade * 1.50
    case _:
        total = 0.00
        print("Código inválido. Insira um código entre 1 e 5.")
print(f"Foi consumido {quantidade} unidades do item {codigo_item}. O Total a pagar é: R$ {total:.2f}")

