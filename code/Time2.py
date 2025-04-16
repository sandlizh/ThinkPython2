"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Time:
    """Represents the time of day as seconds since midnight."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a Time object, storing total seconds."""
        self.seconds = hour * 3600 + minute * 60 + second

    def __str__(self):
        """Returns a string representation of the time."""
        hour, rem = divmod(self.seconds, 3600)
        minute, second = divmod(rem, 60)
        return f"{hour:02d}:{minute:02d}:{second:02d}"

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Returns seconds since midnight."""
        return self.seconds

    def is_after(self, other):
        """Returns True if this time is after other."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds a Time object or a number of seconds."""
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Enables sum() and reversed addition with numbers."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two Time objects."""
        assert self.is_valid() and other.is_valid()
        return int_to_time(self.seconds + other.seconds)

    def increment(self, seconds):
        """Returns a new Time object offset by seconds."""
        return int_to_time(self.seconds + seconds)

    def is_valid(self):
        """Checks whether Time object is valid (0 <= seconds < 86400)."""
        return 0 <= self.seconds < 24 * 3600


def int_to_time(seconds):
    """Creates a new Time object from seconds since midnight."""
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, second)


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
