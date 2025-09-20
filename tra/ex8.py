ant1 = 1
ant2 = 0

nt = int(input("Digite a quantidade de termos da série Fibonacci: "))

print("Termos:")

for cont in range(1, nt -1, 1):
    novo = ant1 + ant2
    print(novo, end=' ')
    ant2 = ant1
    ant1 = novo