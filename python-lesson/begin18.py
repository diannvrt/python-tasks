#Даны три точки A, B, C на числовой оси. 
# Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC.
A = float(input('Введите A: '))
B = float(input('Введите B: '))
C = float(input('Введите C: '))
AC = abs(C - A)
BC = abs(C - B)
total = AC * BC
print(f'Произведение длин отрезков: {total}')