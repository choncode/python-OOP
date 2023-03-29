import pytest
from src.high_score_table import HighScoreTable

def test_returns_limit_property_when_called():
    expected = 3
    high_scores = HighScoreTable(3, [])
    result = high_scores.limit
    print(f'result is {result}')
    assert result == expected

def test_returns_list_when_scores_invoked():
    expected = []
    high_scores = HighScoreTable(3, [])
    result = high_scores.scores
    print(f'result is {result}')
    assert result == expected

def test_returns_updated_scores_when_update_invoked():
    expected = [{'player': 'Cat', 'score': 95}]
    high_scores = HighScoreTable(3, [])
    high_scores.update({'player':'Cat', 'score':95})
    result = high_scores.scores
    print(f'result is {result}')
    assert result == expected

def test_returns_updated_scores_when_update_invoked_more_than_once():
    expected = [{'player': 'Verity', 'score': 150}, {'player': 'Joe', 'score': 120}, {'player': 'Cat', 'score': 95}]
    high_scores = HighScoreTable(3, [])
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'Joe', 'score':120})
    result = high_scores.scores
    print(f'result is {result}')
    assert result == expected

def test_returns_updated_scores_when_update_invoked_more_than_limit():
    expected = [{'player': 'Verity', 'score': 150}, {'player': 'Duncan', 'score': 140}, {'player': 'Alex', 'score': 135}]
    high_scores = HighScoreTable(3, [])
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'Joe', 'score':120})
    high_scores.update({'player':'Alex', 'score':135})
    high_scores.update({'player':'Duncan', 'score':140})
    result = high_scores.scores
    print(f'result is {result}')
    assert result == expected

def test_returns_average_score_of_high_scores():
    expected = 142
    high_scores = HighScoreTable(3, [])
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'Joe', 'score':120})
    high_scores.update({'player':'Alex', 'score':135})
    high_scores.update({'player':'Duncan', 'score':140})
    high_scores.average_score()
    result = high_scores.average_score()
    print(f'result is {result}')
    assert result == expected

def test_returns_highest_score():
    expected = {'player': 'Verity', 'score': 150}
    high_scores = HighScoreTable(3, [])
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'Joe', 'score':120})
    high_scores.update({'player':'Alex', 'score':135})
    high_scores.update({'player':'Duncan', 'score':140})
    high_scores.highest_scorer()
    result = high_scores.highest_scorer()
    print(f'result is {result}')
    assert result == expected

def test_returns_error_if_scores_is_empty_when_highest_scorer_invoked():
    expected = 'there are no high scores in scores'
    high_scores = HighScoreTable(3, [])
    high_scores.highest_scorer()
    result = high_scores.highest_scorer()
    print(f'result is {result}')
    assert result == expected

def test_returns_error_if_scores_is_empty_when_lowest_scorer_invoked():
    expected = 'there are no high scores in scores'
    high_scores = HighScoreTable(3, [])
    high_scores.lowest_scorer()
    result = high_scores.lowest_scorer()
    print(f'result is {result}')
    assert result == expected

def test_returns_lowest_scorer():
    expected = {'player': 'Alex', 'score': 135}
    high_scores = HighScoreTable(3, [])
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'Joe', 'score':120})
    high_scores.update({'player':'Alex', 'score':135})
    high_scores.update({'player':'Duncan', 'score':140})
    high_scores.lowest_scorer()
    result = high_scores.lowest_scorer()
    print(f'result is {result}')
    assert result == expected

def test_returns_score_as_empty_after_rest():
    expected = []
    high_scores = HighScoreTable(3, [])
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'Joe', 'score':120})
    high_scores.update({'player':'Alex', 'score':135})
    high_scores.update({'player':'Duncan', 'score':140})
    high_scores.reset()
    result = high_scores.scores
    print(f'result is {result}')
    assert result == expected

def test_returns_error_if_score_is_empty():
    expected = 'unable to reset as there are no high scores'
    high_scores = HighScoreTable(3, [])
    high_scores.reset()
    result = high_scores.reset()
    print(f'result is {result}')
    assert result == expected





