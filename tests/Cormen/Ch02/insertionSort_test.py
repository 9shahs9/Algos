import Cormen.Ch02.InsertionSort as algos


def test_insertion_sort():
    A = [5,3,4,2,1]
    B = algos.insertion_sort(A)
    result = [1,2,3,4,5]
    assert len(B) == len(result)
    assert B != result
