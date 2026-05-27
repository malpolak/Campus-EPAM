"""
1. Implement a function that flatten incoming data:
=> non-iterables and elements from iterables (any nesting depth should be supported)
=> function should return an iterator (generator function)
=> don't use third-party libraries"""

# Ad1. OPTION I

def merge_elems(*elems):
    for elem in elems:

        # if it is list, tuple, set
        if isinstance(elem, (list, tuple, set)):

            for sub in merge_elems(*elem):
                yield sub

        # if string → split into characters
        elif isinstance(elem, str):

            for ch in elem:
                yield ch

        # if non-iterable
        else:
            yield elem

# example input

a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

##output: 1 2 3 6 z h a b a 1 2 3 4

# Ad 1. OPTION II

from collections.abc import Iterable

def merge_elems_2(*elems):
    for elem in elems:

        # treat single character strings as atomic values
        if isinstance(elem, str) and len(elem) == 1:
            yield elem

        # recursively flatten iterables
        elif isinstance(elem, Iterable):
            yield from merge_elems_2(*elem)

        # yield atomic values
        else:
            yield elem

print("\n" "\n" "option 2")

for _ in merge_elems_2(a, b, c, d):
    print(_, end=' ')

