#Дан список A из N чисел и индекс K (с 0). Вывести A[K], последний элемент и число элементов
# перед элементом с индексом K
N = int(input())

A = []
for i in range(N):
    x = int(input())
    A.append(x)

K = int(input())

print(A[K])
print(A[-1])
print(K)
