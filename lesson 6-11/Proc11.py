#Функция minmax(x, y) возвращает пару (меньшее, большее). Четырьмя вызовами найти минимум и максимум четырёх данных чисел A, B, C, D
def minmax(x, y):
    if x < y:
        return x, y
    return y, x

a = float(input())
b = float(input())
c = float(input())
d = float(input())

min_ab, max_ab = minmax(a, b)
min_cd, max_cd = minmax(c, d)
min_all = minmax(min_ab, min_cd)[0]
max_all = minmax(max_ab, max_cd)[1]
print(min_all)
print(max_all)