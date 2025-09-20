'''
adivinhação gere um núm aleatório de 1 a 20 e permita tentativas ilimitadas até acerto, mostrando dicas maior/menor
 '''
import random
import math

num_secreto = random.randint(1,20)
tentativas = 0

while True:
    palpite = int(input("Adivinhe um número entre 1 e 20: "))
    tentativas += 1
    if palpite < num_secreto:
        print("Muito baixo")
    elif palpite > num_secreto:
        print("Muito alto")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas")