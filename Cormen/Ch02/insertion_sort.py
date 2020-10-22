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


def insertion_sort_2dot3_4(A):
    """

    :param A:
    :return:

    recursive version of the insertion sort.
    """
    if len(A)==1:
        return A
    key = A[len(A)-1]
    sorted_A = insertion_sort_2dot3_4(A[:len(A)-1])


    j = len(A)-1
    i = j -1
    while i!=j and j >=0 and i>=0:
        if key > sorted_A[i]:
            A[j] = key
        else:
            A[j] = sorted_A[i]
            i = i-1
        j = j-1
    if i<0 and j>=0:
        A[j] = key
        j = j-1
    while j>=0:
        A[j] = sorted_A[j]
        j = j-1

    return A




if __name__ == "__main__":
    A = [5,3,4,1,2]
    print(A)
    actual = insertion_sort_2dot3_4(A)
    print(actual)