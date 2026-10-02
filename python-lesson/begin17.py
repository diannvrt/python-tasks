#Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.
A = float(input('Введите A: '))
B = float(input('Введите B: '))
C = float(input('Введите C: '))
AC = abs(C - A)
BC = abs(C - B)
total = AC + BC
print(f'Длина отрезка AC: {AC}')
print(f'Длина отрезка BC: {BC}')
print(f'Сумма отрезков: {total}')