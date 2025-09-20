import math

# Definir o número total de alunos (n) e o tamanho da equipe (k)
n = 12
k = 4

# Calcular o número de combinações
numero_de_equipes = math.comb(n, k)

# O resultado é armazenado na variável 'numero_de_equipes'
print(f"Podem ser formadas {numero_de_equipes} equipes diferentes de 4 alunos a partir de uma sala com 12 alunos.")