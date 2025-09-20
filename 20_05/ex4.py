cont = 0
n = int(input("Informe um número inteiro positivo: "))

for i in range( 0, n + 1):
    soma = i ** 2
    cont += soma

print(f"A soma dos quadrados dos números até {n} é : {cont}")