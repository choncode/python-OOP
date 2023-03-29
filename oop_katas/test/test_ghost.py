import pytest

from src.ghost import ( Ghost, Blinky, Pinky, Inky, Clyde )

def test_returns_name_property():
    ghost = Ghost('Ducky', 3, 'yellow')
    assert ghost.name == 'Ducky'

def test_returns_speed_property():
    ghost = Ghost('Ducky', 3, 'yellow')
    assert ghost.speed == 3

def test_returns_colour_property():
    ghost = Ghost('Ducky', 3, 'yellow')
    assert ghost.colour == 'yellow'

def test_returns_is_scared_as_false_by_default():
    ghost = Ghost('Ducky', 3, 'yellow')
    assert ghost.is_scared() == False

def test_returns_can_be_eaten_as_false_by_default():
    ghost = Ghost('Ducky', 3, 'yellow')
    assert ghost.can_be_eaten() == False

def test_returns_can_be_eaten_as_true_when_is_frighten_called():
    mack = Ghost('Mack', 9, 'grey')
    assert mack.colour == 'grey'
    assert mack.is_scared() == False
    assert mack.can_be_eaten() == False
    mack.frighten()
    assert mack.colour == 'blue'
    assert mack.is_scared() == True
    assert mack.can_be_eaten() == True


def test_returns_can_be_eaten_as_true_when_is_frighten_called():
    jersey = Ghost('Jersey', 3, 'white')
    jersey.speed_up()
    assert jersey.speed == 3.3
    jersey.speed_up()
    assert jersey.speed == 3.63
    jersey.speed_up()
    assert jersey.speed == 3.993

def test_returns_new_class_blinky():
    blinky = Blinky('Blinky', 3,'red')
    assert blinky.colour == 'red'
    blinky.frighten()
    assert blinky.colour == 'blue'
    assert blinky.is_scared == True
    assert blinky.can_be_eaten == True




