''' Média dinâmica: leia números inteiros até o usuário digitar -1; exiba média
e quantidade.
'''
soma = 0 
quantidade = 0
num = 0

while (num != -1):
    num = int(input("Informe um número inteiro.\nCaso queira sair  do loop digite '-1': "))
    soma += num
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média foi de {media}. A quantidade foi de {quantidade}")
else:
    print("Não foi digitado nenhum número!")
