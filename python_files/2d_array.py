#!/usr/bin/env python3

"""2D array."""

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]


def hourglassSum(arr):
    """Get hourglass sum and print max."""
    max_hr = None

    for i in range(len(arr)):
        for j in range(len(arr) - 3):
            hr = (
                arr[i][i:i + 3]
                + arr[i + 1][i:i + 3]
                + arr[i + 2][i:i + 3]
            )

            hr = sum(hr)

            if not max_hr or hr > max_hr:
                max_hr = hr

            print(f"{hr = }")
            print(f"{max_hr = }")

    return max_hr


hourglassSum(arr)
