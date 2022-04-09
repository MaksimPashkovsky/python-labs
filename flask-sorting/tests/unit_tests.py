import unittest
from sorting import shaker_sort, insertion_sort, selection_sort, heap_sort
from hashing import hash_list
from typing import Callable


def sorting_function_test(sorting_function: Callable):
    data = [1, 3, 6, 8, 1, 2, 0, 0, 0]
    output = sorting_function(data)
    assert output == sorted(data)

    data = [3, 36, -9, 26, 85, -26, 78, -82, 8, 60]
    output = sorting_function(data)
    assert output == sorted(data)

    data = [3.0, 36.23, -9.102, 26.002, 85.3, -26.4, 78.909, -82, 8.1, 60.22]
    output = sorting_function(data)
    assert output == sorted(data)

    data = []
    output = sorting_function(data)
    assert output == []


class TestSortingFunctions(unittest.TestCase):

    def test_shaker_sort(self):
        sorting_function_test(shaker_sort)

    def test_insertion_sort(self):
        sorting_function_test(insertion_sort)

    def test_selection_sort(self):
        sorting_function_test(selection_sort)

    def test_heap_sort(self):
        sorting_function_test(heap_sort)

    def test_equal_output(self):
        data = [1, 3, 6, 8, 1, 2, 0, 0, 0]
        assert shaker_sort(data) == insertion_sort(data) == selection_sort(data) == heap_sort(data)

        data = [3, 36, -9, 26, 85, -26, 78, -82, 8, 60]
        assert shaker_sort(data) == insertion_sort(data) == selection_sort(data) == heap_sort(data)

        data = [3.0, 36.23, -9.102, 26.002, 85.3, -26.4, 78.909, -82, 8.1, 60.22]
        assert shaker_sort(data) == insertion_sort(data) == selection_sort(data) == heap_sort(data)

        data = []
        assert shaker_sort(data) == insertion_sort(data) == selection_sort(data) == heap_sort(data)


class TestHashFunction(unittest.TestCase):

    def test_hash_list(self):
        a = []
        assert hash_list(a) == hash_list(a)

        a = [2]
        assert hash_list(a) == hash_list(a)

        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert hash_list(a) == hash_list(a)

        a = [0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 1]
        assert hash_list(a) != hash_list(b)

        a = [1.2, 3.4, 5.6, 7.8, 9.10, 11.12]
        b = [1.2, 3.4, 5.6, 7.8, 9.10, 11.11]
        assert hash_list(a) != hash_list(b)


if __name__ == '__main__':
    unittest.main()
