#Дана строка S. Если S — допустимое имя файла, создать пустой файл с этим именем и вывести True, иначе False
import os

s = input()
try:
    with open(s, 'w', encoding='utf-8') as f:
        pass
    print('True')
    os.remove(s)
except (OSError, ValueError):
    print('False')