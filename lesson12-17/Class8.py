#Класс Hero: name, health, damage; методы to_dict() и from_dict(data); сохранить объект в словарь, создать из словаря новый объект и вывести его health
class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'damage': self.damage
        }
    
    @staticmethod
    def from_dict(data):
        return Hero(data['name'], data['health'], data['damage'])
    
h1 = Hero('Рыцарь', 100, 25)
data = h1.to_dict()
h2 = Hero.from_dict(data)

print(h2.health)