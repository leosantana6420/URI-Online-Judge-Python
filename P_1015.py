import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distancia = pow((x2 - x1), 2) + pow((y2 - y1), 2)

distancia_total = math.sqrt(distancia)

print('{:.4f}'.format(distancia_total))