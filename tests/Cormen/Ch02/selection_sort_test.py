import Cormen.Ch02.selection_sort as algo

def test_selection_sort():
    A = [31, 41, 59, 26, 41, 58]
    actual = algo.selection_sort(A)
    expected = [26,31,41,41,58,59]
    assert actual == expected
    assert len(actual) == len(expected)
