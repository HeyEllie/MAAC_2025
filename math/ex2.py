impar = 1
par = 1
n = 0

n = int(input("Informe um número inteiro positivo: "))

for i in range (1, n+1):
    if i %2 == 0:
        par *= i
    else:
        impar *= i

print(f"O produtos dos número inteiros pares de 1 até {n} é: {par}")
print(f"O produtos dos número inteiros ímpares de 1 até {n} é: {impar}")
