#Даны имена двух файлов: первый существует и непуст, второй отсутствует. Создать второй и записать в него первый и последний элементы первого
name1 = input()
name2 = input()

with open(name1, encoding='utf-8') as f:
    lines = f.readlines()
    
with open(name2, 'w', encoding='utf-8') as f:
    f.write(lines[0])
    f.write(lines[-1])
    