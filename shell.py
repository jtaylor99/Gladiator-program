import core


def get_name_and_assign_stats():
    name_1 = input('What\'s your name?')
    print('Welcome to the Game of Gladiators!', name_1.upper(), '!')
    name_2 = input('What\'s your name?')
    print('Welcome to the Game of Gladiators!', name_2.upper(), '!')
    name_1 = core.new_gladiator(name_1, 100, 0, 10, 20)
    name_2 = core.new_gladiator(name_2, 100, 0, 10, 20)
    return name_1, name_2


def gladiator_turn(name_1, name_2):
    print('{} turn'.format(name_1['Name'].upper()))
    while True:

        print('>>>>[A]ttack')
        print('>>>>[H]eal')
        print('>>>>[P]ass')
        print('>>>>[Q]uit')
        action = input('{} What would you like to do?'.format(
            name_1['Name'].upper()))
        if action == 'A':
            print(name_1['Name'], 'Attacks')
            core.attack(name_1, name_2)
            print('{} health is now at:{}'.format(name_2['Name'].upper(),
                                                  name_2['health']))
            return None
        if action == 'H':
            print(name_1['Name'], 'Heals')
            core.heal(name_1)
            print('{} health is now at:{}'.format(name_1['Name'].upper(),
                                                  name_1['health']))

            return None
        if action == 'P':
            break
        if action == 'Q':
            quit()
        else:
            print('Please choose a valid option!')


def main():
    name_1, name_2 = get_name_and_assign_stats()
    while True:
        gladiator_turn(name_1, name_2)
        gladiator_turn(name_2, name_1)


if __name__ == '__main__':
    main()
