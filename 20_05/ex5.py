cont  = 0 
cont1  = 0 

n = int(input("Informe um número inteiro positivo: "))
for i in range (0, n + 1):
    if i ** 2 == n:
        cont += i
        print(f"O número {n} tem um quadrado perfeito: {cont}")
    else:
        if i ** 2 != n:
            cont1 += i
            print(f"O número {n} não tem um quadrado perfeito: {cont1}")