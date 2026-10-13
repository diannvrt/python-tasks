#Та же задача, что Err5, но с двумя ветками: нечисловой индекс — «Ошибка ввода»,
# индекс вне границ — «Нет такого символа».
try:
    text = str(input())
    symbol = int(input())
    print(text[symbol])
except IndexError:
    print('Нет такого символа')
except ValueError:
    print('Ошибка ввода')