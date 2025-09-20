'''
PEça ao user para digitar um num. inteiro positivo N e calcule a soma de todos os múltiplos de 3 de 1 até N
'''
soma = 0

n = int(input("Informe um número inteiro positivo: "))
for i in range(3, n+ 1, 3):
    soma += i
    print(f"A soma dos múltiplos de três até {n} é: {soma}")

