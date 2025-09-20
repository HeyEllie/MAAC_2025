soma = 0 

print("Digite 10 números: ")
for i in range(1, 10,1):
   num = int(input(f"Digite o {i}° número: "))
   if num**2 < 255:
    soma += num

print(f"A soma dos números cujos quadrados são menores que 255 é: {soma}")