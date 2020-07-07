#!/usr/bin/env python3

"""Trying to recreate algorithm question on interview exam."""

from collections import Counter


def solution(A, B):
    """Return number of letters required for A and B, non-empty strings in all lowercase, to be annograms."""
    counter = 0

    if (A := sorted(A)) == (B := sorted(B)):
        return print(counter)
    else:
        A = Counter(A)
        B = Counter(B)

        for k in A:
            if not B[k]:
                counter += A[k]
            elif A[k] != B[k]:
                counter += abs(A[k] - B[k])

        for k in B:
            if not A[k]:
                counter += B[k]

        return print(counter)


solution("lemon", "melon")  # 0
solution("lemon", "mdelvonnf")  # 4
solution("lemo", "melon")  # 1
solution("hiremike", "mikehire")  # 0
solution("hgsirerjmike", "mikesddferhire")  # 6
