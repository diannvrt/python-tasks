#================================================
#ИГРА «ПОДЗЕМЕЛЬЕ: ТИХАЯ ТАЙНА»
#Автор: Vartanova Diana
#Дата: сентябрь 2026
#
# Пункт 4 — «прислушаться»: герой замирает
# и слушает, что происходит в темноте. Пытается прочувствовать атмосферу. Пока
# пункт только выводится в меню - обрабатывать
# его будем на третьем занятии.
# ================================================

# --- Заголовок ------------------------------------
title = "ПОДЗЕМЕЛЬЕ: ТИХАЯ ТАЙНА"
frame = "=" * 25
print(frame)
print(" " + title + " ")
print(frame)
print()


print('Как зовут героя?')
hero_name = input()

print(f'Добро пожаловать, {hero_name}!')
print('Ты входишь в подземелье.. Спускаешься в узкий каменный проход. Перед тобой огромная пещера.')
print()

print('Что делаешь?')
print('1 - осмотреться')
print('2 - идти вперед')
print('3 - отдохнуть')
print('4 - Прислушаться')
print('5 - зажечь факел')
print()

choice = input()

title = "Удачи"
frame = "=" * 25
print(frame)
print(f'{title}, {hero_name}')
print(frame)
print()

print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
luck = int(input())

base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2

stamina = (agility + health) // 2

print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Удача: {luck}")

print()

print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")

print()
