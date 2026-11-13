#Функция sort_dec3(a, b, c) возвращает три значения по убыванию. Упорядочить два набора

def sort_dec3(a, b, c):
    x, y, z = sorted([a, b, c], reverse=True)
    return x, y, z

a1 = float(input())
b1 = float(input())
c1 = float(input())
p1, q1, r1 = sort_dec3(a1, b1, c1)
print(p1)
print(q1)
print(r1)

a2 = float(input())
b2 = float(input())
c2 = float(input())
p2, q2, r2 = sort_dec3(a2, b2, c2)
print(p2)
print(q2)
print(r2)