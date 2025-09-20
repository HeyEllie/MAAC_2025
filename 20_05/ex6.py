soma = 0


n = int(input("Informe um número inteiro positivo: "))

if n <= 0:
    print("Digite um número inteiro positivo!")
else:
    for i in range ( 1, n +1 ):
        soma += (1/i)

print(f"A soma da série harmônica é: {soma}")