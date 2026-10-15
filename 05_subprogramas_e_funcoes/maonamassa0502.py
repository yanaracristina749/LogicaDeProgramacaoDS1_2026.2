# TODO: Crie a função lambda aqui
calcular_acrescimo = None # Substitua pela expressão lambda

# Teste
calcular_acrescimo = lambda salario : salario * 1.10
salario = float(input("Digite o salário: R$"))
novo_salario = calcular_acrescimo(salario)

print (f"Salário com acréscimo de 10%: R${novo_salario:.2f}")