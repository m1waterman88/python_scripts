#!/usr/bin/env python3

"""This is a bunch of nonsense that let's me play with values."""


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


def print_from_stream(number, stream=EvenStream()):
    for _ in range(number):
        print(stream.get_next())

    # Need to add this
    stream.current = 0


queries = ["odd 2", "even 3", "odd 5"]
# queries = ["even 2", "even 3", "even 5"]

for i in range(len(queries)):
    stream_name, number = queries[i].split()
    number = int(number)

    if ((stream_name == "even" and number % 2 != 0)
            or (stream_name == "odd" and number % 2 == 0)):
        print(f"Mismatched stream name and number: {stream_name} {number}")
        continue

    if stream_name == "even":
        print_from_stream(number)
    else:
        print_from_stream(number, OddStream())
