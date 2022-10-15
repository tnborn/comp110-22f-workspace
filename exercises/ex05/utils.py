"""EX05 - Utility Functions."""
__author__ = "730563181"


def only_evens(input: list[int]) -> list[int]:
    """Given list, return new list of evens."""
    result = []

    for i in range(len(input)):
        if (input[i] % 2) == 0: 
            result.append(input[i])
    print(result)
    return result


def concat(input1: list[int], input2: list[int]) -> list[int]:
    """Given two lists, generate new list with elements from both lists."""
    result = list()

    for i in range(len(input1)):
        result.append(input1[i])
    for i in range(len(input2)):
        result.append(input2[i])
    print(result)
    return result


def sub(input1: list[int], start: int, end: int) -> list[int]:
    """Given list, start and end index, generate subset list."""
    result = list()

    if start < 0:
        start = 0
    if end > (len(input1)):
        end = len(input1)
    if len(input1) == 0:
        print(result)
        return result
    elif start > len(input1):    
        print(result)
        return result
    elif end <= 0:
        print(result)
        return result
    else:
        for i in range(start, end):
            result.append(input1[i])
        print(result)
        return result
