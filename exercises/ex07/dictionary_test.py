"""EX07 - Tests for the dictionary functions."""
__author__ = "730563181"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_empty_invert() -> None:
    """Edge case that tests if invert will invert keys and value in empty."""
    empty: dict[str, str] = {}
    assert invert(empty) == {}


def test_single_invert() -> None:
    """Use case to test if invert will invert key and value of string in single."""
    single: dict[str, str] = {'c': 'x'}
    assert invert(single) == {'x': 'c'}


def test_multiple_invert() -> None:
    """Use case to test if invert will invert key and value in multiple value dictionary."""
    multiple: dict[str, str] = {'a': 'z', 'b': 'y'}
    assert invert(multiple) == {'z': 'a', 'y': 'b'}


def test_empty_favorite_color() -> None:
    """Edge case that tests for most frequent favorite_color in empty."""
    empty: dict[str, str] = {}
    assert favorite_color(empty) == ""


def test_single_favorite_color() -> None:
    """Use case to test for most frequent favorite_color in single."""
    single: dict[str, str] = {"Kris": "blue"}
    assert favorite_color(single) == 'blue'


def test_multiple_favorite_color() -> None:
    """Use case to test for most frequent favorite_color in multiple value dictionary."""
    multiple: dict[str, str] = {"Kris": "blue", "Ezri": "blue", "Marc": "yellow"}
    assert favorite_color(multiple) == 'blue'


def test_empty_count() -> None:
    """Edge case that tests if count of the number of times a value appears is the given."""
    empty: list[str] = []
    assert count(empty) == {}


def test_single_count() -> None:
    """Use case that tests if count works in single."""
    single: list[str] = ["blue"]
    assert count(single) == {'blue': 1}


def test_multiple_count() -> None:
    """Use case that tests if count will count multiple items from dictionary."""
    multiple: list[str] = ["red", "blue", "red"]
    assert count(multiple) == {'red': 2, 'blue': 1}