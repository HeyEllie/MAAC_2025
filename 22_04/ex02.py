n = int(input("Digite a quantidade de termos (n) da PG:" ))
a = float(input("Digite o valor do primeiro termo PG (a): "))
r = float(input("Digite a razão (r) da PG: "))

print("\n Os", n, "primeiros termos da P.G são: ")

for i in range(n):
    termo = a * (r ** i)
print(f"Termo {i+1}: {termo}")
