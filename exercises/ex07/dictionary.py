"""EX07 - Dictionary Functions."""
__author__ = "730563181"


def invert(keys: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary keys and values."""
    diction = {}
    for i in keys:
        if keys[i] in diction:
            raise KeyError("Key Error!")
        diction[keys[i]] = i
    return diction


def favorite_color(given: dict[str, str]) -> str:
    """Returns the color that appeared the most frequent from given input."""
    diction: dict[str, int] = {}
    maximum: int = 0
    most_often_color: str = ""
    for i in given:
        if given[i] in diction:
            diction[given[i]] += 1
        else:
            diction[given[i]] = 1
    for i in diction:
        if diction[i] > maximum:
            most_often_color = i
            maximum = diction[i]
    return most_often_color


def count(given: list[str]) -> dict[str, int]:
    """Returns  a dictionary of the counts of each of the items in the input list."""
    diction: dict[str, int] = {}
    for i in given:
        if i in diction:
            diction[i] += 1
        else:
            diction[i] = 1
    return diction