"""EX04 - Utils."""
__author__ = "730563181"


def all(input: list[int], check_value: int) -> bool:
    """Checking if all values are true, false, or other."""
    result: bool = False
    for i in range(len(input)):
        if input[i] == check_value:
            result = True
        else: 
            result = False  
            break
    if result is True:
        print("True") 
    elif len(input) == 0:
        print("The input list is empty")
    else:
        print("False")
    return result


def max(input: list[int]) -> int:
    """Given list, return largest."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    
    result: int = input[0]
    result_neg: int = 0
    
    # Check for all negatives
    for i in range(len(input) - 1):
        if input[i] < 0:
            # add up the elements and see if it is negative, if so do another if statement that checks the smallest     
            result_neg += input[i]
    for i in range(len(input) - 1):
        if input[i] > input[i + 1] and result_neg >= 0:
            if input[i] > result:
                result = input[i]    
        elif input[i] < input[i + 1] and result_neg >= 0:
            if input[i + 1] > result:
                result = input[i + 1]
        elif result_neg < 0 and input[i] > input[i + 1]:
            if input[i] >= result:
                result = input[i]
        elif result_neg < 0 and input[i] < input[i + 1]: 
            if input[i + 1] >= result:
                result = input[i + 1]
    print(result)
    return result


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Returning true if there is index match in lists."""
    result: bool = False
    if len(input1) == len(input2) and (len(input1) != 0 or len(input2) != 0):
        if len(input1) == 1:
            for i in range(len(input1)):
                if input1[i - 1] == input2[i - 1]:
                    result = True
                else:
                    result = False 
        else:
            for i in range(len(input1) - 1):
                if input1[i] == input2[i]:
                    result = True
                else:
                    result = False
    elif len(input1) == 0 and len(input2) == 0:
        print("The two lists are empty, but they are the same.")
        result = True
    else:
        print("The two lists are not the same length.")
    if len(input1) == len(input2) and (len(input1) != 0 or len(input2) != 0):
        if (result is True):
            print("True")
        else:
            print("False") 
    return result