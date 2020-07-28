#!/usr/bin/env python3

"""Using zip."""

n, x = map(int, input().split())
subject = []

for _ in range(x):
    subject.append(map(float, input().split()))

for score in zip(*subject):
    print(sum(score) / x)


"""
# example input
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

# correct output for example input
90.0
91.0
82.0
90.0
85.5
"""
