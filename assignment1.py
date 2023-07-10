# Name: Shuyao Zeng
# OSU Email: zengs@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1
# Due Date: 07/11/2023
# Description: This is a python fundamental review with ten different classes using a class
#              StaticArray. They are required to be implemented with certain complexity.


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    TODO: Return a tuple of the minimum and maximum values of the given array.
    """
    min_num = arr[0]
    max_num = arr[0]
    for index in range(arr.length()):
        if arr[index] < min_num:
            min_num = arr[index]
        elif arr[index] > max_num:
            max_num = arr[index]
    return min_num, max_num

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    TODO: Return a new array with string "fizz" if the number in the original array is
          divisible by 3, with string "buzz" if the number in the original array is
          divisible by 5, and string "fizzbuzz" if the number in the original array is
          both a multiple of 3 and a multiple of 5.
    """
    new_arr = StaticArray(arr.length())
    for index in range(arr.length()):
        if arr[index] % 3 == 0 and arr[index] % 5 == 0:
            new_arr[index] = "fizzbuzz"
        elif arr[index] % 3 == 0:
            new_arr[index] = "fizz"
        elif arr[index] % 5 == 0:
            new_arr[index] = "buzz"
        else:
            new_arr[index] = arr[index]
    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    TODO: Reserve the order of the elements in the given array.
    """
    for index in range(arr.length() // 2):
        temp = arr[index]
        arr[index] = arr[arr.length() - 1 - index]
        arr[arr.length() -1 - index] = temp

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Return a new array with all of the elements from the original array
          which are shifted right or left given steps number of times.
    """
    new_arr = StaticArray(arr.length())
    for index in range(arr.length()):
        if steps > 0:
            move = (index + steps) % arr.length()
            new_arr[move] = arr[index]
        elif steps < 0:
            move = (index + steps + arr.length()) % arr.length()
            new_arr[move] = arr[index]
        else:
            new_arr[index] = arr[index]
    return new_arr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Returns an array that contains all the consecutive integers between
          given start and end (inclusive).
    """
    length = abs(start - end) + 1
    new_arr = StaticArray(length)
    if start <= end:
        for index in range(length):
            new_arr[index] = start + index
    if start > end:
        for index in range(length):
            new_arr[index] = start - index
    return new_arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Return 1 if the given array is sorted in strictly ascending order.
          Return -1 if the list is sorted in strictly descending order.
          Return 0 otherwise.
    """
    ascending = 0
    descending = 0
    if arr.length() == 1:
        return 1
    else:
        for index in range(arr.length() - 1):
            if arr[index] < arr[index + 1]:
                ascending += 1
            elif arr[index] > arr[index + 1]:
                descending += 1
        if ascending == arr.length() - 1:
            return 1
        elif descending == arr.length() - 1:
            return -1
        else:
            return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    TODO: Return a tuple of the mode of the given array and its frequency. If there
          is more than one element that has the highest frequency, select the one
          that occurs first in the array.
    """
    count = 1
    mode = arr[0]
    frequency = 1
    for index in range(1, arr.length()):
        if arr[index] == arr[index - 1]:
            count += 1
            if count > frequency:
                mode = arr[index]
                frequency = count
        else:
            count = 1
    return mode, frequency

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Return a new array with all duplicate values removed.
    """
    repeat = 0
    for index in range(1, arr.length()):
        if arr[index] == arr[index - 1]:
            repeat += 1
    new_arr = StaticArray(arr.length() - repeat)
    new_arr[0] = arr[0]
    count = 0
    for index in range(1, arr.length()):
        if arr[index] == arr[index - 1]:
            count += 1
        else:
            new_arr[index - count] = arr[index]
    return new_arr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Return a new array with the same content of the given array sorted
          in non-ascending order.
    """
    min_num = min_max(arr)[0]
    max_num = min_max(arr)[1]
    num_range = max_num - min_num + 1
    count_arr = StaticArray(num_range)
    new_arr = StaticArray(arr.length())
    for index in range(num_range):
        count_arr[index] = 0
    for index in range(arr.length()):
        count_arr[num_range - (arr[index] - min_num) - 1] += 1
    for index in range(1, num_range):
        count_arr[index] += count_arr[index - 1]
    for index in range(arr.length()):
        new_arr[count_arr[num_range - (arr[index] - min_num) - 1] - 1] = arr[index]
        count_arr[num_range - (arr[index] - min_num) - 1] -= 1
    return new_arr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Return a new array with squares of the values from the given array,
          sorted in non-descending order.
    """
    new_arr = StaticArray(arr.length())
    count = arr.length() - 1
    left = 0
    right = arr.length() - 1 - left
    for index in range(arr.length()):
        if abs(arr[left]) < abs(arr[right]):
            new_arr[count] = arr[right] ** 2
            count -= 1
            right -= 1
        else:
            new_arr[count] = arr[left] ** 2
            count -= 1
            left += 1
    return new_arr

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
