n = 0
a = 0
r = 0


n = int(input("Informe a quantidade de termos: "))
a = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão: "))

print(f"Os {n} primeiros termos da P.G. são:")

for i in range(0, n, 1): # ele vai ir do num 0 ao num que o usuário entrar, e vai ir indo de um em um
    t = a * (r**i)
    print(f"Termo {i+1}: {t}")