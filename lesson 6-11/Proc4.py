#Функция triangle_ps(a) возвращает периметр P = 3·a и площадь S = a2·√3/4 равностороннего треугольника. Найти P и S трёх данных сторон
def triangle_ps(a):
    P = 3 * a
    S = a ** 2 * (3 ** 0.5 / 4) 
    return P, S

for i in range(3):
    a = float(input())
    P, S = triangle_ps(a)
    print(P)
    print(S)
    