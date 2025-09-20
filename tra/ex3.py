mi = 0

for i in range(1, 11, 1):
    id = int(input("digite a idade da pessoa: "))
    if ( mi == 0 or id < mi):
        mi = id

print(f"A maior idade informada foi: {mi}")

