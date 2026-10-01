"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade_visitante = int(input("Digite a idade do visitante: "))
if idade_visitante < 12:
    tipo_bilhete = "Infantil"
    valor_final = 100.00 * 0.50
elif idade_visitante >= 60:
    tipo_bilhete = "Melhor Idade"
    valor_final = 0.00
else:
    tipo_bilhete = "Integral"
    valor_final = 100.00


print(f"Tipo de bilhete: {tipo_bilhete}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
