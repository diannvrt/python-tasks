#Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
a = float(input('Введите a: '))
b = float(input('Введите b: '))
total = a ** 2 + b ** 2
diff = a ** 2 - b ** 2
product = a ** 2 * b ** 2
quotient = a ** 2 / b ** 2
print(f'Сумма квадратов: {total}')
print(f'Разность квадратов: {diff}')
print(f'Произведение квадратов: {product}')
print(f'Частное квадратов: {quotient}')