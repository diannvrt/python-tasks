#Даны M, N, число D и набор из M чисел. Первый столбец — набор; каждый следующий столбец равен предыдущему плюс D по строкам
m = int(input())
n = int(input())
d = int(input())

values = []
for i in range(m):
    values.append(int(input()))

a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(values[i] + d * j)
    a.append(row)
    
for row in a:
    print(row)
    