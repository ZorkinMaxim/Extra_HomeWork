# Два участника p1 и p2 учавствую в дуэли
# Напишите функцию whos_first, которая принимает две строки и возвращает имя игрока, который выстрелил первым.
# Если игроки выстрелили одновременно, то вернуть строку "tie"

def whos_first(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        return "tie"


print(whos_first('   Bang', '    Bang'))
print(whos_first('    Bang', '    Bang'))
print(whos_first('    Bang', '  Bang'))
