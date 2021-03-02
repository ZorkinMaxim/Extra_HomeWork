# Написать игру в "камень - ножницы - бумага" против компьютера.
# Запустить игу в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага).
# Сгенерировать случайный выбор компьютера. Вывести выбор компьютера.
# Определить победителя, выведя соответствующую информацию. Спросить пользователя - хочет ли он повторить игру.
# Если хочет - повторить. Если не хочет - выйти из цикла.

import random

should_continue = True

while should_continue:
    player_choice = input('Player choice: [R/S/P]').lower()
    if player_choice not in ['r', 's', 'p']:
        print('Incorrect input. Try again.')
        continue
    gen = {1: 'r', 2: 's', 3: 'p'}
    comp_choice = gen[random.randint(1, 3)]
#variation 2: comp_choice = random.choice(['r', 's', 'p'])

    print(f'Comp choice = {comp_choice}')
    winning_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]
    if player_choice == comp_choice:
        print('A draw')
    elif (player_choice, comp_choice) in winning_combinations:
        print('Player wins')
    else:
        print('Comp wins')
    should_continue = input('Do you want to try your luck one more time?').lower() == 'y'
