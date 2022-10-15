"""EX05 - Utility Functions Test."""
__author__ = "730563181"

from ex05.utils import only_evens


from ex05.utils import concat


from ex05.utils import sub


def test_only_evens_items() -> None:
    """Testing a few ints."""
    input: list[int] = [1, 2, 3]    
    assert only_evens(input) == [2]


def test_only_evens_many_items() -> None:
    """Testing more ints."""
    input: list[int] = [1, 5, 3]
    assert only_evens(input) == []


def test_only_evens_many_items_again() -> None:
    """Testing different ints."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_concat_items() -> None:
    """Testing concat with ints."""
    input: list[int] = [1, 2, 3]    
    assert concat(input) == [2]


def test_concat_many_items() -> None:
    """Testing concat with other ints."""
    input: list[int] = [1, 5, 3]
    assert concat(input) == []


def test_concat_many_items_again() -> None:
    """Testing with other ints."""
    assert concat([4, 4, 4]) == [4, 4, 4]


def test_sub_items() -> None:
    """Testing sub from example."""
    input: list[int] = [10, 20, 30, 40]    
    assert sub(input) == [20, 30]


def test_sub_many_items() -> None:
    """Testing sub with ints."""
    input: list[int] = [1, 5, 3]
    assert sub(input) == []


def test_sub_many_items_again() -> None:
    """Testing sub with different ints."""
    assert sub([4, 4, 4]) == [4, 4, 4]
