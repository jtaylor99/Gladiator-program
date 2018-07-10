import core


def get_name():
    name_1 = input('What\'s your name?')
    print('Welcome to the Game of Gladiators!', name.upper(), '!')
    return name


def get_name2():
    name_2 = input('What\'s your name?')
    print('Welcome to the Game of Gladiators!', name.upper(), '!')
    return name


def gladiator_1_turn():
    print('{} turn'.format(get_name()))
    while True:
        action = input('What would you like to do?')
        print('>>>>Attack')
        print('>>>>Heal')
        print('>>>>Pass')
        print('>>>>Quit')
    if action.lower == 'Attack':
        core.attack(gladiator_2)
    if action.lower == 'Heal':
        core.heal(gladiator_1)
    if action.lower == 'Pass':
        break
    if action.lower == 'Quit':
        quit()
    else:
        print('Please choose a valid option!')

def gladiator_2_turn():
