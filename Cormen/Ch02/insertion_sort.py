def _insertion_sort_desc(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key > A[i]:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

def _insertion_sort_asc(A):

    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and key < A[i]:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


def insertion_sort(A, order):
    if order == 0:
        return _insertion_sort_asc(A)
    elif order == 1:
        return _insertion_sort_desc(A)
