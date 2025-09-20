n = int(input("Informe um número inteiro positivo: "))

tr = 0
for n in range (1, n+1, 1):
    tr += n

print(f"O número triângular de {n} é: {tr}")