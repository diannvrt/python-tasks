# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ»
# Автор: Диана Вартанова
# Дата: сентябрь 2026
#
# Пункт 4 — «прислушаться»: герой замирает
# и слушает, что происходит в темноте. Пока
# пункт только выводится в меню — обрабатывать
# его будем на третьем занятии.
# ================================================

import random
import dungeon
import json
import os
try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

#-------Заголовок-----------------------------------
VERSION = '1.0'
title = "ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ"
frame = "=" * 31

#-------Функции-------------------------------------

def parse_command(line):
    '''Возвращает пару (verb, words): глагол и слова команды.'''
    cmd = line.strip().lower()
    words = cmd.split()
    if not words:
        return '', []
    verb = words[0]
    if cmd in num_to_verb:
        verb = num_to_verb[cmd]
    return verb, words

def write_save(hero, gold_total, actions, enemies, hero_r, hero_c, visited, found_loot):
    '''Собирает состояние и пишет в save.json'''
    save = {
        'hero': hero.to_dict(),
        'gold': gold_total,
        'actions': actions,
        'enemies': enemies,
        'position': [hero_r, hero_c],
        'visited': [list(p) for p in visited],
        'loot': sorted(found_loot)
    }
    with open('save.json', 'w', encoding='utf-8') as f:
        json.dump(save, f, ensure_ascii=False, indent=2)
        
def print_leaderboard(log):
    if not log:
        print("You haven't fought yet")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print('Leaderboard (hero damage):')
    for i in range(len(top)):
        print(f'{i + 1}. Round {top[i][0]}: {top[i][1]:.1f}')
    worst = max(log, key=lambda r: r[2])
    print(f'Strongest enemy hit: {worst[2]} (round {worst[0]}).')
    
def print_run_summary(log):
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f'Damage: {total:.1f} across {rounds} rounds, average {total / rounds:.1f}.')
    else:
        print('No battles this run.')
        
def scout(r, c, seen):
    if (r, c) in seen or MAP[r][c] == '#':
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total
MAP = [
        ['#', '#', '#', '#', '#'],
        ['#', '.', '.', '#', '#'],
        ['#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '#'],
        ['#', '#', 'S', '.', '#']
    ]
DIRECTIONS = {'north': (-1, 0), 'south': (1, 0), 'west': (0, -1), 'east': (0, 1)}
LOOT = {(1, 1): "old coin", (2, 3): "dusty potion", (3, 3): "guard's gem"}
num_to_verb = {'1': 'look', '2': 'go', '3': 'rest', '4': 'listen', '5': 'torch', '6': 'train', '7': 'descend', '8': 'leaders', '9': 'shop', '10': 'backpack', '11': 'drink', '0': 'exit'}


#-------Начало игры-----------------------
print(frame)
print(" " + title + " ")
print(frame)
print()
loaded = None
max_health = 100
if os.path.exists('save.json'):
    print('A save was found. Continue the run? (yes/no)')
    answer = input().strip().lower()
    if answer == 'yes':
        try:
            with open('save.json', encoding='utf-8') as f:
                loaded = json.load(f)
        except json.JSONDecodeError:
            print('Save file is corrupted. Starting a new run.')
            loaded = None
if loaded is None:
    print('Как зовут героя?')
    hero_name = input()
    print(f'Добро пожаловать, {hero_name}!')
    print('Ты входишь в подземелье. Здесь темно и пахнет сыростью.')
    print()

# --- Настройка героя -------------------------------
    print("Настройка героя.")
    print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
    while True:
        try:
            health = int(input())
            strength = int(input())
            agility = int(input())
            endurance = int(input())
            if health <= 0:
                raise ValueError(f'Здоровье должно быть положительным, а введено {health}.')
            if strength < 0 or agility < 0 or endurance < 0:
                raise ValueError('Характеристики не могут быть отрицательными')
            break
        except ValueError as e:
            print(f'{e}. Введите все четыре числа заново: ')
    print()
    
    hero = dungeon.Hero(hero_name, health, strength, agility, endurance)
    max_health = health
    print(hero)
    print()
    enemies = ['ghoul', 'skeleton', 'spider', 'bat']
    inventory = {}
    gold_total = 0
    ability_bonus = 0
    log = []
    actions = 0
    hero_r, hero_c = 4, 2
    visited = {(4, 2)}
    found_loot = set()
else:
    hero = dungeon.Hero.from_dict(loaded['hero'])
    max_health = hero.health
    gold_total = loaded['gold']
    actions = loaded['actions']
    enemies = loaded['enemies']
    hero_r, hero_c = loaded['position']
    visited = {tuple(p) for p in loaded['visited']}
    found_loot = set(loaded['loot'])
    inventory = {}
    ability_bonus = 0
    log = []
    print(f'Run continued: health {hero.health}, gold {gold_total}, enemies left {len(enemies)}.')
commands = ['look', 'go', 'rest', 'listen', 'torch', 'train', 'descend', 'leaders', 'shop', 'backpack', 'drink potion', 'buy <item> [count]', 'exit', 'map', 'scout', 'go <direction>', 'newgame']
MENU = ['What do you do? (number or command; help for help)', '1 - look around (look)', '2 - go forward (go)', '3 - rest (rest)', '4 - listen (listen)', '5 - light a torch (torch)', '6 - train (train)', '7 - descend deeper (descend)', '8 - leaderboard (leaders)', '9 - shop (shop)', '10 - backpack (backpack)', '11 - drink potion (drink)', '0 - exit the dungeon (exit)', 'map, scout, go north/south/west/east, newgame']
running = True
outcome = 'прерывание'

try:
    while running:
        print('\n'.join(MENU))
        print()
        line = input()
        verb, words = parse_command(line)
        while verb == '':
            print('Empty command. Type a command or number')
            line = input()
            verb, words = parse_command(line)
        
        match verb:
            case 'exit':
                print('Вы поднимаетесь обратно к свету. Подземелье остается позади.')
                write_save(hero, gold_total, actions, enemies, hero_r, hero_c, visited, found_loot)
                print('Progress saved.')
                outcome = 'выход'
                running = False
            case 'newgame':
                if os.path.exists('save.json'):
                    os.remove('save.json')
                    print('Save destroyed. The next run starts fresh.')
                else:
                    print('No save to destroy.')
                continue
            case 'look':
                print('Вы осмотрелись. Комната пуста, только пыль на полу.')
            case 'go':
                if len(words) > 1 and words[1] in DIRECTIONS:
                    dr, dc = DIRECTIONS[words[1]]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != '#':
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        print(f'You step {words[1]}. Room ({hero_r}, {hero_c}).')
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f'You found {item}! Unique loot: {len(found_loot)}.')
                    else:
                        print(f'Cannot go {words[1]}: wall or edge.')
                else:
                    on_fumes = hero.spend_stamina(2)
                    if on_fumes:
                        print('Сил больше нет - вы идёте на упорстве.')
                    else:
                        print('Вы осторожно идёте вперёд. Пол скрипит под ногами.')
            case 'rest':
                hero.stamina = min(hero.stamina + 5, max_health // 10 + hero.endurance)
                print('Вы присели отдохнуть. Силы понемногу возвращаются.')
            case 'listen':
                print('Вы замерли и прислушались. Где-то капает вода.')
            case 'torch':
                hero.stamina -= 1
                print('Вы зажгли факел. Стало светлее, но огонь требует сил.')
            case 'train':
                strikes = 5
                hero.spend_stamina(3)
                print('Вы подходите к тренировочному чучелу')
                print('Оно стоит здесь с тех пор, как сюда приходил последний искатель.')
                print()
                print(f'Наносите {strikes} ударов')
                total_damage = 0
                crit_count = 0
                for i in range(1, strikes + 1):
                    hit_damage, crit = hero.strike(i)
                    if crit:
                        crit_count += 1
                        print(f'Удар {i}: {hit_damage:.1f} - критический!')
                    else:
                        print(f'Удар {i}: {hit_damage:.1f}')
                    total_damage += hit_damage
                print()
                print(f'Итог {strikes} ударов, критических ударов: {crit_count}.')
                print(f'Общий урон: {total_damage:.1f}')
                print(f'Средний урон: {total_damage / strikes:.1f}')
            case 'descend':
                if not enemies:
                    print('But the dungeon is empty.')
                else:
                    enemy_name = random.choice(enemies)
                    foe = dungeon.Enemy(enemy_name, dungeon.enemy_stats[enemy_name])
                    rounds, won, loot = dungeon.fight(foe, hero, ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy_name)
                        print(f'{enemy_name.capitalize()} defeated! {len(enemies)} enemies left in the dungeon. Loot: {loot} gold.')
                        print(f'Battle: {len(rounds)} rounds.')
            case 'leaders':
                print_leaderboard(log)
            case 'shop':
                print('Shop:')
                for name, price in dungeon.prices.items():
                    print(f'{name}: {price} gold')
                print('Use: buy <item> [count]')
            case 'backpack':
                if not inventory: 
                    print('Backpack is empty')
                else:
                    print('Backpack:')
                    for name, qty in inventory.items():
                        print(f'{name}: {qty} pcs')
            case 'buy':
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = ' '.join(words[1:-1])
                else:
                    qty = 1
                    item = ' '.join(words[1:])
                if item == '':
                    print('Buy what? Type: buy <item>.')
                    continue
                if item not in dungeon.prices:
                    print('No such item in the shop.')
                    continue
                gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    print(f'Bought {qty} {item} for {dungeon.prices[item] * qty} gold. Gold left: {gold_total}.')
                else:
                    print(f'Not enough gold: need {dungeon.prices[item] * qty}, have {gold_total}.')
            case 'drink':
                item = ' '.join(words[1:]) or 'potion'
                if inventory.get(item, 0) == 0:
                    print(f'No {item} in the backpack.')
                else:
                    hero.heal(10, max_health)
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f'You drink a {item}. Health: {hero.health}. Potions left: {inventory.get(item, 0)}.')
            case 'help':
                print('Commands: ' + ', '.join(commands) + '.')
                print('Numbers 0-11 work as before.')
            case 'map':
                print('Map:')
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = '@' if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(' '.join(cells))
            case 'scout':
                seen = set()
                print(f'Scout: {scout(hero_r, hero_c, seen)} rooms reachable')
            case _:
                print(f"Don't understand command: '{line.strip()}'. Type 'help'.")
                continue
        
                
        if hero.health <= 0:
            print(f'{hero.name} падает без сил. Подземелье забирает еще одного искателя.')
            if os.path.exists('save.json'):
                os.remove('save.json')
            outcome = 'гибель'
            running = False
        if running:
            actions += 1
        print()
        
        state = f'Health: {hero.health} | Stamina: {hero.stamina} | Enemies left: {len(enemies)} | Gold: {gold_total}'
        if COLOR: 
            print(Fore.GREEN + state + Style.RESET_ALL) 
        else:
            print(state)
except KeyboardInterrupt:
    print()
    print('Игрок прервал сеанс.') 
    write_save(hero, gold_total, actions, enemies, hero_r, hero_c, visited, found_loot)   

finally:
    print(frame)
    if outcome == 'гибель':
        print(f'Ты не дошел, {hero.name}. Действий совершено: {actions}.')
    elif outcome == 'выход':
        print(f'Забег окончен, {hero.name}. Действий совершено: {actions}.')
    else:
        print(f'Сеанс прерван, {hero.name}. Действий совершено: {actions}.')
    
    if inventory:
        print('Left behind in the backpack:')
        for name, qty in inventory.items():
            print(f'{name}: {qty} pcs')
    else:
        print('Left behind in the backpack: nothing.')
    
#------ Итоговая статистика -----------------------
    print_run_summary(log)
    print(frame)