n = 0


n = int(input("Informe um número para calcular o fatorial: "))

if n < 0:
    print("Não existe fatorial de número negativo.")
else:
    f = 1
    for i in range(1,n+1,1):
        f = f * i

print(f"O fatorial de {n} é: {f}")