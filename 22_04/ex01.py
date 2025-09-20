
num =  int(input("Digite um número para calcular o fatorial: "))

if num < 0:
    print("Não existe fatorial de número negativo!!")
else:
    fatorial = 1
    for i in range (1, num + 1):
        fatorial = fatorial * 1
    print(f"O fatorial de {num} é {fatorial}")