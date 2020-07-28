#!/usr/bin/env python3

"""Debug default-value error."""


class EvenStream(object):

    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):

    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())
    # Need to add this
    stream.current = 0


"""
queries = int(input())
for _ in range(queries):
    # stream_name, n = input().split()
    stream_name, n = "odd 2", ("even 3"), ("odd 5")
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
"""

queries = ["odd 2", "even 3", "odd 5"]
# queries = ["even 2", "even 3", "even 5"]
for i in range(len(queries)):
    stream_name, n = queries[i].split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
