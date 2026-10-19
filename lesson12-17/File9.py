#Даны имена двух файлов: один существует и непуст (не обязательно первый), другой отсутствует. Создать отсутствующий и записать в него конечный и начальный элементы существующего
import os

name1 = input()
name2 = input()

if os.path.exists(name1):
    existing_file = name1
    missing_file = name2
else:
    existing_file = name2
    missing_file = name1
    
with open(existing_file, encoding='utf-8') as f:
    lines = f.readlines()

with open(missing_file, 'w', encoding='utf-8') as f:
    f.write(lines[-1])
    f.write(lines[0])
    