from collections import OrderedDict

from loto.players import Player
from loto.game import Game
from start import create_players, validate_answer, validate_count


def test_game():
    """
    Проверка создания класса игры
    """
    g = create_players()
    assert type(g) == Game


def test_validate_count():
    """
    Проверка, что вводится число
    """
    assert validate_count("2") == 2
    assert validate_count("2345") == 2345
    assert validate_count("dwadwadwds") == False


def test_validate_answer():
    """
    Проверка, что вводится число
    """
    assert validate_answer("y") == True
    assert validate_answer("n") == False
    assert validate_answer("dwadwadwds") == None


def test_create_card():
    """
    Проверка, что карточка игрока создается правильнол
    """
    p = Player("Test 1")
    assert type(p.card) == OrderedDict
    assert len(p.card) == 15
    for number, value in p.card.items():
        assert type(number) == int
        assert number < 91
        assert number >= 1
        assert value == True


def test_check_card():
    """
    Проверка определения победителя
    """
    p = Player("Test 1")
    for number in p.card:
        p.card[number] = False
    assert p.check_card() == True
