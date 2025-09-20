soma = 0

n = int(input("Número pra ver se é triangular: "))

# COMEÇA A CONTAGEM
contador = 1

# FAZ A SOMA ATÉ PASSAR DO NÚMERO
while soma < n:
    soma += contador  # SOMA
    contador += 1     # AVANÇA

# VERIFICA E FALA O RESULTADO
if soma == n:
    print(f"O {n} É triangular!")
else:
    print(f"O {n} NÃO é triangular.")