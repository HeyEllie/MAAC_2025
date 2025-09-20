p_impares = 1

n = int(input("informe um número inteiro positivo: "))
if n <= 0:
    print("Digite um número inteiro positivo!")
else:
    for i in range(1, n + 1):
        if i % 2 != 0:
            p_impares *= i  # Multiplica o produto acumulado pelo número ímpar

print(f"O produto de todos os números ímpares de 1 até {n} é: {p_impares}")