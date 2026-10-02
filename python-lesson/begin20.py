#Найти расстояние между двумя точками с заданными координатами (x1, y1) и
# (x2, y2) на плоскости. Расстояние вычисляется по формуле √((x2 − x1)2 + (y2 − y1)2).

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
A = abs(x2 - x1)
B = abs(y2 - y1)
distance = (A ** 2 + B ** 2) ** 0.5
print(distance)