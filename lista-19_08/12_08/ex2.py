"senha secreta com até 3 tentativas"
senha_correta = 'python123'
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha correta: ")
    if senha == senha_correta:
        print("senha correta: acesso concedido")
        break
    else: 
        print("senha incorreta") 
        tentativas += 1
    if tentativas == max_tentativas:
        print("Número máximo de tentativas excendido")