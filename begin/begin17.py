# №17 Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.
a = float(input('Введите точку a: '))
b = float(input('Введите точку b: '))
c = float(input('Введите точку c: '))

ac = abs(c - a)
bc = abs(c - b)
sum = ac + bc

print(f'Длина отрезка AC = {ac}')
print(f'Длина отрезка BC = {bc}')
print(f'Сумма отрезков = {sum}')
