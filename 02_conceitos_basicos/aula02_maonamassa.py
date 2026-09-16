# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string
amigos =  int (input("quantos amigos está presente no restaurante?"))
conta =  float (input ("qual valor final da conta?"))
resutado = float(conta)/int(amigos)
print(f"{resutado:.2f}")
