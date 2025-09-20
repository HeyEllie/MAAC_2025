'''
Calcule a área de um triângulo retângulo de catetos 6 e 8 usando Pitágoras
'''
import math

def calcular_area_triangulo(cateto1, cateto2):
  """
  Calcula a área de um triângulo retângulo.

  Args:
    cateto1: O comprimento de um dos catetos.
    cateto2: O comprimento do outro cateto.

  Returns:
    A área do triângulo.
  """
  return (cateto1 * cateto2) / 2

def calcular_hipotenusa_pitagoras(cateto1, cateto2):
  """
  Calcula a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras.

  Args:
    cateto1: O comprimento de um dos catetos.
    cateto2: O comprimento do outro cateto.

  Returns:
    O comprimento da hipotenusa.
  """
  # Calcula a soma dos quadrados dos catetos
  soma_quadrados = math.pow(cateto1, 2) + math.pow(cateto2, 2)    #math.pow(x, y) → potência (x^y)
  # Retorna a raiz quadrada da soma dos quadrados para obter a hipotenusa
  return math.sqrt(soma_quadrados)  #math.sqrt(x) → raiz quadrada de x

# Exemplo de uso:
cateto_a = 6
cateto_b = 8

area = calcular_area_triangulo(cateto_a, cateto_b)
hipotenusa = calcular_hipotenusa_pitagoras(cateto_a, cateto_b)

print(f"Os catetos são: {cateto_a} e {cateto_b}")
print(f"A área do triângulo é: {area}") # Saída: A área do triângulo é: 6.0
print(f"A hipotenusa é: {hipotenusa}") # Saída: A hipotenusa é: 5.0