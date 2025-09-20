'''
peça ao user para digitar trÊs números inteiros (A, B e K) e conte quantos números entre A e B õa divisiveis ppor K
'''
cont = 0
a = int(input("Informe o valor inicial A: "))
b = int(input("Informe o valor final B: "))
k = int(input("Informe o valor do divisor K: "))

for i in range (a, b + 1):
    if i % k == 0:
        cont += 1
        
print(f"Números divisiveis por {k} entre {a} e {b} é: {cont}")