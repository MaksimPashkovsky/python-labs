"""
Numbers wrapper
"""

import operator
from typing import Type


class NumbersWrapper:

    def __init__(self, *args):
        self.numbers = list(args)

    def __len__(self):
        return len(self.numbers)

    @classmethod
    def _build_operated(cls, nums1: list[int], nums2: list[int], operator) -> 'NumbersWrapper':
        len1, len2 = len(nums1), len(nums2)
        m = max(len1, len2)
        l1 = nums1 + [0] * (m - len1)
        l2 = nums2 + [0] * (m - len2)
        res = [operator(x, y) for x, y in zip(l1, l2)]
        return cls(*res)

    def __add__(self, other):
        return self._build_operated(self.numbers, other.numbers, operator.add)

    def __sub__(self, other):
        return self._build_operated(self.numbers, other.numbers, operator.sub)

    def __mul__(self, other):
        return self._build_operated(self.numbers, other.numbers, operator.mul)

    def __truediv__(self, other):
        return self._build_operated(self.numbers, other.numbers, operator.truediv)

    def __floordiv__(self, other):
        return self._build_operated(self.numbers, other.numbers, operator.floordiv)

    def __mod__(self, other):
        return self._build_operated(self.numbers, other.numbers, operator.mod)

    def __pow__(self, power, modulo=None):
        res = [n ** power for n in self.numbers]
        return NumbersWrapper(*res)

    def __gt__(self, other):
        return self.numbers > other.numbers

    def __ge__(self, other):
        return self.numbers >= other.numbers

    def __lt__(self, other):
        return self.numbers < other.numbers

    def __le__(self, other):
        return self.numbers <= other.numbers

    def __eq__(self, other):
        return self.numbers == other.numbers

    def __ne__(self, other):
        return self.numbers != other.numbers

    def append(self, number):
        self.numbers.append(number)

    def __setitem__(self, key, value):
        self.numbers[key] = value

    def __repr__(self):
        return f"NumbersWrapper({self.numbers})"


if __name__ == '__main__':
    n1 = NumbersWrapper(1, 2, 3)
    n1.append(4)
    print(n1)
    n1[2] = 99
    print(n1)

    # tests
    assert (NumbersWrapper(1, 2, 3) + NumbersWrapper(3, 4, 5)).numbers == [4, 6, 8]
    assert (NumbersWrapper(1, 2, -3, 12) + NumbersWrapper(3, 4, 5)).numbers == [4, 6, 2, 12]
    assert (NumbersWrapper() + NumbersWrapper(3, 4, 5)).numbers == [3, 4, 5]

    assert (NumbersWrapper(3, 4, 5) - NumbersWrapper(1, 2, 3)).numbers == [2, 2, 2]
    assert (NumbersWrapper(0, 4, -8) - NumbersWrapper(1, 2, 3)).numbers == [-1, 2, -11]
    assert (NumbersWrapper(-3, 4, -5) - NumbersWrapper(1, 2, 3, 10)).numbers == [-4, 2, -8, -10]

    assert (NumbersWrapper(3, 4, 5) * NumbersWrapper(1, 2, 3)).numbers == [3, 8, 15]
    assert (NumbersWrapper(1, 2, 3) * NumbersWrapper(3, 4, 5)).numbers == [3, 8, 15]
    assert (NumbersWrapper(1, 2, 3, 0) * NumbersWrapper(3, 4, 5)).numbers == [3, 8, 15, 0]

    assert (NumbersWrapper(3, 4, 5) / NumbersWrapper(3, 4, 5)).numbers == [1, 1, 1]
    assert (NumbersWrapper(32, 40, 52) / NumbersWrapper(8, 5, 2, 1)).numbers == [4, 8, 26, 0]
    assert (NumbersWrapper(3, 4, 5) / NumbersWrapper(-3, -4, -5)).numbers == [-1, -1, -1]

    assert (NumbersWrapper(3, 4, 5) // NumbersWrapper(3, 4, 5)).numbers == [1, 1, 1]
    assert (NumbersWrapper(32, 40, 52) // NumbersWrapper(10, 4, 50, 1)).numbers == [3, 10, 1, 0]
    assert (NumbersWrapper(3, 4, 5) // NumbersWrapper(-3, -4, -5)).numbers == [-1, -1, -1]

    assert (NumbersWrapper(3, 4, 5) % NumbersWrapper(3, 4, 5)).numbers == [0, 0, 0]
    assert (NumbersWrapper(32, 40, 52) % NumbersWrapper(10, 4, 50, 1)).numbers == [2, 0, 2, 0]
    assert (NumbersWrapper(3, 4, 5) % NumbersWrapper(2, 10, 4)).numbers == [1, 4, 1]

    assert (NumbersWrapper(3, 4, 5) ** 1).numbers == [3, 4, 5]
    assert (NumbersWrapper(3, 4, 5) ** 0).numbers == [1, 1, 1]
    assert (NumbersWrapper(3, 4, 5) ** 2).numbers == [9, 16, 25]
    assert (NumbersWrapper(1, 4, 9) ** 0.5).numbers == [1, 2, 3]

    assert len(NumbersWrapper(1, 2, 3)) == 3
    assert len(NumbersWrapper()) == 0

    assert (NumbersWrapper(1, 2, 3) > NumbersWrapper(3, 4, 5)) is False
    assert (NumbersWrapper(1, 2, 3, 8) > NumbersWrapper(3, 4, 5)) is False
    assert (NumbersWrapper() > NumbersWrapper(3, 4, 5)) is False
    assert (NumbersWrapper(1, 2, 3) > NumbersWrapper(1, 2, 3)) is False
    print("All tests passed")
