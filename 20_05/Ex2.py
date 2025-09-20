'''
Peça ao user para digitar um num. inteiro positivo N e calcule  a diferença  entre a soma
dos numeros pares e a soma dos números impares de 1 até  N
'''
n = 0
soma_pares = 0
soma_impares = 0

n - int(input("Informe um número inteiro positivo: "))
for i in range (1, n + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print(f"A diferença entre pares e ímpares é: {soma_pares - soma_impares}")