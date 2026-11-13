#Класс Inventory: словарь предметов в __init__; методы add(name, qty) и total() (сумма количеств); вывести total после трёх добавлений
class Inventory:
    def __init__(self):
        self.items = {}
        
    def add(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty
    
    def total(self):
        return sum(self.items.values())
    
inv = Inventory()

for i in range(3):
    name = input()
    qty = int(input())
    inv.add(name, qty)

print(inv.total())