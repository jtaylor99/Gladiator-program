from random import randint


def new_gladiator(gladiator_name, health, rage, damage_low, damage_high,
                  level):
    return {
        'Name': gladiator_name,
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high,
        'level': level
    }


def attack(attacker, defender):
    damage = randint(attacker['damage_low'], attacker['damage_high'])

    miss_roll = randint(1, 5)
    if miss_roll == 1:
        return 'miss'
    evade_roll = randint(1, 6)
    if evade_roll == 1:
        return 'evade'
    crit_roll = randint(1, 100)
    if crit_roll < attacker['rage']:
        crit_damage = damage * 2
        defender['health'] = defender['health'] - crit_damage
        return 'crit'
    else:
        defender['health'] = defender['health'] - damage
        attacker['rage'] = attacker['rage'] + 15
        return 'hit'


def leveled_up(gladiator):
    gladiator['level'] += 1
    if gladiator['rage'] == 60 and gladiator['level'] > 1:
        gladiator['level'] + 1
        gladiator['health'] + 10
        gladiator['damage_low'] + 10
        gladiator['damage_high'] + 10
        gladiator['rage'] == 0
        return gladiator['level']


def heal(gladiator):
    if gladiator['rage'] >= 10 and gladiator['health'] <= 95:
        gladiator['health'] = gladiator['health'] + 20
        gladiator['rage'] = gladiator['rage'] - 10
        return gladiator['health']
    else:
        return None


def is_dead(gladiator):
    if ['health'] == 0:
        return True
    else:
        return False
