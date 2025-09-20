'''8. Fração Simplificada 
Simplifique a fração 168/252. 
math.gcd(a, b) calcula o máximo divisor comum (MDC). 
Dividimos numerador e denominador pelo MDC. 
 '''
import math


# Calcula o MDC entre o numerador e o denominador
mdc_valor = math.gcd(168, 252)

# Simplifica a fração dividindo ambos por seu MDC
numerador_simplificado = 168 // mdc_valor
denominador_simplificado = 252 // mdc_valor

# Imprime o resultado
print(f"A fração original é 168/252 e seu MDC é: {mdc_valor}")
print(f"A fração simplificada é: {numerador_simplificado}/{denominador_simplificado}")