#!/usr/bin/env python3

"""
https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""

import random
random.__file__

print(random.__file__)


def bubble_sort(arr: list[int]) -> list[int]:
    """Sort arr with bubble sort."""
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x += 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr


'''
arr = random.sample(range(1, 200), 100)
print("", "Before bubble sort:", "-"*50, arr, sep="\n")
bubble_sort(arr)
print("","", "After bubble sort:", "-"*50, arr, sep="\n")
'''


def selection_sort(arr: list[int]) -> list[int]:
    """Sort arr with selection sort."""
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # place it at the front of the assorted array
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


'''
arr = random.sample(range(1, 200), 100)
print("", "Before selection sort:", "-"*50, arr, sep="\n")
bubble_sort(arr)
print("","", "After selection sort:", "-"*50, arr, sep="\n")
'''


def insertion_sort(arr: list[int]) -> list[int]:
    """Sort arr with insertion sort."""
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # swap the number down the list
            arr[pos] = arr[pos - 1]
            pos -= 1
        # break and do the final swap
        arr[pos] = cursor

    return arr


'''
arr = random.sample(range(1, 200), 100)
print("", "Before insertion sort:", "-"*50, arr, sep="\n")
bubble_sort(arr)
print("","", "After insertion sort:", "-"*50, arr, sep="\n")
'''


def merge_sort(arr: list[int]) -> list[int]:
    """Sort arr with merge sort."""
    # print("Splitting ", arr)

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # recursion
        merge_sort(left_half)
        merge_sort(right_half)

        L, R, A = 0, 0, 0

        while L < len(left_half) and R < len(right_half):
            if left_half[L] < right_half[R]:
                arr[A] = left_half[L]
                L += 1
            else:
                arr[A] = right_half[R]
                R += 1
            A += 1

        while L < len(left_half):
            arr[A] = left_half[L]
            L += 1
            A += 1

        while R < len(right_half):
            arr[A] = right_half[R]
            R += 1
            A += 1

    # print("Merging ", arr)


'''
arr = random.sample(range(1, 200), 100)
print("", "Before merge sort:", "-"*50, arr, sep="\n")
bubble_sort(arr)
print("","", "After merge sort:", "-"*50, arr, sep="\n")
'''

# quick sort


'''
arr = random.sample(range(1, 200), 100)
print("", "Before quick sort:", "-"*50, arr, sep="\n")
bubble_sort(arr)
print("","", "After quick sort:", "-"*50, arr, sep="\n")
'''
