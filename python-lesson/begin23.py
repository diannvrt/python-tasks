#Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B,
# B — в C, C — в A, и вывести новые значения переменных A, B, C.
A = int(input('Введите A: '))
B = int(input('Введите B: '))
C = int(input('Введите C: '))
temp = A
A = C
C = B
B = temp
print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')