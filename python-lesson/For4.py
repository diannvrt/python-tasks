#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.
price_1kg = float(input())
for i in range(1, 11):
    cost = price_1kg * i
    print(cost)