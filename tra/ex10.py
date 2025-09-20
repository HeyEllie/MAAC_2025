sp = 0
cn = 0
 

print("Digite 10 números: ")
for i in range(1, 10,1):
   num = int(input(f"Digite o {i}° número: "))
   if num > 0:
    sp +=sp + num
   else:
    if num < 0:
        cn += cn + 1

print(f"A soma dos números positivos é: {sp}")
print(f"O total de números negativos é: {cn}")
