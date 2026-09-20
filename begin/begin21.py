# №21 Даны координаты трёх вершин треугольника. Найти его периметр и
# площадь. Использовать формулу для расстояния между двумя
# точками (см. Begin20). Для площади — формулу Герона: S = √(p·(p −a)·(p − b)·(p − c)),
# где p = (a + b + c)/2 — полупериметр, a, b, c — стороны.
# d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) print(d)
import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

a = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
b = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
c = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

perimeter = a + b + c
p = perimeter / 2

s = math.sqrt(abs(p * (p - a) * (p - b) * (p - c)))
print(perimeter)
print(s)
