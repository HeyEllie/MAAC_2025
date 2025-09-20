'''
Sequência de Fibonacci: solicite n e imprima os n primeiros termos da série.
'''
ultimo = 1
penultimo = 0

n = int(input("Digite a quantidade de termos da série Fibonacci: "))
count=0
while count < n:
    if count == 0:
        print(0)
    elif count == 1:
        print(1)
    else:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo)
    count += 1

# if (n==0):
#     print("0")
# elif n == 1:
#     print("1")
# else:
#     count=0
#     while count < n:
#         termo = ultimo + penultimo
#         penultimo = ultimo
#         ultimo = termo
#         count += 1
#         print(termo, "\n")



