from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    return {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }


def attack(attacker, defender):
    crit_roll = randint(1, 100)
    if crit_roll <= attacker['rage']:
        crit_damage = damage * 2
    else:
        attacker['rage'] == 0
    damage = randint(attacker['damage_low'], attacker['damage_high'])
    defender['health'] = defender['health'] - damage
    attacker['rage'] = attacker['rage'] + 15



def 
 