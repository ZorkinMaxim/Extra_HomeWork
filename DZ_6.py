# Detect Flush
# Texas Holdem. Определить есть или нет комбинации Flush из 5 карт на столе и 2 карт в руках.

# variation 1
table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

table_suites = [i[-1] for i in table_cards]
hand_suites = [i[-1] for i in hand_cards]

suites_in_game = table_suites + hand_suites

flush = False
for suit in 'CHSD':
    if suites_in_game.count(suit) >= 5:
        flush = True

if flush:
    print('Flush!')
else:
    print('No Flush!')

# variation 2

table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

table_suites = [i[-1] for i in table_cards]
hand_suites = [i[-1] for i in hand_cards]

suites_in_game = table_suites + hand_suites

flush = any([suites_in_game.count(suit) >= 5 for suit in 'CHSD'])

if flush:
    print('Flush!')
else:
    print('No Flush!')

# variation 3

table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

flush = any([sum([card[-1] == suit for card in table_cards + hand_cards]) >= 5 for suit in 'CHSD'])

if flush:
    print('Flush!')
else:
    print('No Flush!')