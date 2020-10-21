import Cormen.Ch02.merge_sort as algo

def test_merge_sort():
    A = [31, 41, 59, 26, 41, 58]
    actual = algo.merge_sort(A)
    expected = [26, 31, 41, 41, 58, 59]
    assert actual == expected
    assert len(actual) == len(expected)