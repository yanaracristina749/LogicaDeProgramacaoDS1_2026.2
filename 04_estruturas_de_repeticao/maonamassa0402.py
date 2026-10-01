# TODO: Desenvolva o acumulador com parada no 0
soma = 0

# Escreva a estrutura de repetição while
soma = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        break

    soma += numero

print(f"Soma: {soma}")
