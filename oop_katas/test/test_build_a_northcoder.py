# make sure to import and install pytest
# make sure to import your class

import pytest
from src.build_a_northcoder import Northcoder

def test_returns_first_value_as_correct_name():
    expected = 'Alex'
    alex = Northcoder('Alex', 'Manchester', 'Data Engineer', 'March 2020')
    result = alex.name
    print(f'result is {result}')
    assert result == expected

def test_returns_second_value_as_correct_location():
    expected = 'Manchester'
    bashir = Northcoder('Alex', 'Manchester', 'Data Engineer', 'March 2020')
    result = bashir.location
    print(f'result is {result}')
    assert result == expected

def test_returns_third_value_as_correct_course():
    expected = 'Data Engineer'
    alex = Northcoder('Alex', 'Manchester', 'Data Engineer', 'March 2020')
    result = alex.course
    print(f'result is {result}')
    assert result == expected

def test_returns_fourth_value_as_correct_graduation_date():
    expected = 'March 2020'
    alex = Northcoder('Alex', 'Manchester', 'Data Engineer', 'March 2020')
    result = alex.graduation_date
    print(f'result is {result}')
    assert result == expected

def test_returns_greet_method():
    expected = 'Hello Joe, my name is Alex'
    alex = Northcoder('Alex', 'Manchester', 'Data Engineer', 'March 2020')
    result = alex.greet('Joe')
    print(f'result is {result}')
    assert result == expected

def test_returns_graduation_date_method_with_boolean():
    expected = True
    alex = Northcoder('Alex', 'Manchester', 'Data Engineer', 'March 2020')
    result = alex.alumni()
    print(f'result is {result}')
    assert result == expected


