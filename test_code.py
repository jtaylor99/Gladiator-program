from core import *


def test_new_gladiator1():
    result = new_gladiator(100, 0, 10, 20)
    assert result == {
        'health': 100,
        'rage': 0,
        'damage_low': 10,
        'damage_high': 20
    }


def test_new_gladiator2():
    result = new_gladiator(50, 30, 10, 20)
    assert result == {
        'health': 50,
        'rage': 30,
        'damage_low': 10,
        'damage_high': 20
    }


def test_attack1():
    gladiator_1 = new_gladiator(100, 0, 20, 20)
    gladiator_2 = new_gladiator(50, 30, 10, 20)
    attack(gladiator_1, gladiator_2)
    assert gladiator_1['rage'] == 15
    assert gladiator_2['health'] == 30


def test_attack2():
    gladiator_1 = new_gladiator(80, 15, 10, 20)
    gladiator_2 = new_gladiator(100, 0, 10, 20)
    attack(gladiator_2, gladiator_1)
    assert gladiator_2['rage'] == 15
    assert attack(gladiator_2, gladiator_1) == gladiator_1['health']


def test_heal1():
    gladiator_1 = new_gladiator(100, 15, 10, 20)
    gladiator_2 = new_gladiator(90, 30, 10, 20)
    heal(gladiator_2)
    assert gladiator_2['health'] == 95
    assert gladiator_2['rage'] == 20


def test_heal2():
    gladiator_1 = new_gladiator(80, 40, 10, 20)
    gladiator_2 = new_gladiator(100, 20, 10, 20)
    heal(gladiator_1)
    assert gladiator_1['health'] == 85
    assert gladiator_1['rage'] == 30


def test_is_dead1():
    gladiator_1 = new_gladiator(0, 50, 20, 30)
    result = is_dead(gladiator_1)
    assert True == True


def test_is_dead2():
    gladiator_1 = new_gladiator(100, 0, 10, 20)
    result = is_dead(gladiator_1)
    assert False == False
