
import Cormen.Ch02.linear_search as algo

def test_linear_search_ex_2dot1_3():
    A = [5,4,6,8,9,10]
    key = 8
    idx = algo.linear_search(A,key)
    assert idx != None
    assert idx == 4
