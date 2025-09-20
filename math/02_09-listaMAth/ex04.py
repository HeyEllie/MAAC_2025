'''7. Corrida de Revezamento 
Numa competição de revezamento, 5 atletas vão correr, mas apenas 3 posições (ordem importa) precisam ser escolhidas. Quantas formações diferentes são possíveis? 

math.perm(n, k) calcula permutações (ordem importa).  '''
import math

print(f"Será possivel fazer {math.perm(5, 3)} posições diferentes")