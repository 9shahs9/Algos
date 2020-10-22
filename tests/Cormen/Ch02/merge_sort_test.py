import Cormen.Ch02.merge_sort as algo
import random

def test_merge_sort():
    A = [31, 41, 59, 26, 41, 58]
    actual = algo.merge_sort(A)
    expected = [26, 31, 41, 41, 58, 59]
    assert actual == expected

def test_merge_sort_depth():
    A = [random.randint(1,100) for i in range(100)]
    expected = sorted(A)
    actual = algo.merge_sort(A)
    assert actual == expected
