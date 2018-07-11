from random import randint


def new_gladiator(gladiator_name, health, rage, damage_low, damage_high):
    return {
        'Name': gladiator_name,
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }


def attack(attacker, defender):
    damage = randint(attacker['damage_low'], attacker['damage_high'])

    miss_roll = randint(1, 5)
    if miss_roll == 1:
        return 'miss'
    crit_roll = randint(1, 100)
    if crit_roll < attacker['rage']:
        crit_damage = damage * 2
        defender['health'] = defender['health'] - crit_damage
        return 'crit'
    else:
        defender['health'] = defender['health'] - damage
        attacker['rage'] = attacker['rage'] + 15
        return 'hit'


def heal(gladiator):
    if gladiator['rage'] >= 10 and gladiator['health'] <= 95:
        gladiator['health'] = gladiator['health'] + 5
        gladiator['rage'] = gladiator['rage'] - 10
        return gladiator['health']
    else:
        return None


def is_dead(gladiator):
    if ['health'] == 0:
        return True
    else:
        return False
