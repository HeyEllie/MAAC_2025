'''Uma colônia de bactérias dobra a cada hora. Se inicialmente havia
200 bactérias, quantas existirão após 5 horas?'''
import math

# Define a população inicial de bactérias
populacao_inicial = 200

# Define o número de horas
horas = 5

# Calcula a população final usando a fórmula de crescimento exponencial
populacao_final = populacao_inicial * math.pow(2, horas)

# Imprime o resultado
print(f"Após {horas} horas, existirão {populacao_final} bactérias.")