"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
# Função para calcular o preço final
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    desconto = preco_base * taxa_desc
    preco_com_desconto = preco_base - desconto
    imposto = preco_com_desconto * taxa_imp
    preco_final = preco_com_desconto + imposto

    return preco_final


# Função para exibir o relatório
def exibir_relatorio_item(numero_item, preco_final):
    print(f"Item {numero_item}: R$ {preco_final:.2f}")

preco1 = calcular_preco_final(100, 0.10, 0.05)
preco2 = calcular_preco_final(250, 0.20, 0.08)
preco3 = calcular_preco_final(80, 0.05, 0.10)

exibir_relatorio_item(1, preco1)
exibir_relatorio_item(2, preco2)
exibir_relatorio_item(3, preco3)