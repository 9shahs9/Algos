

def selection_sort(A):
    """
    :param A: A is the vector of integers to be sorted.
    :return: A sorted vector of integers.

    Loop Invariants :
        The array will be split into three parts
        1) a sorted array on the left,
        2) The next position to be sorted. [index]
        3) The right half of the array which is yet to be sorted.

        Initialisation :
        Initially the first half of the array is a None array, as all the elements are not sorted.
        First position will be index 0,
        Right half of the array is the entire array passed.

        Maintenance :
        The role of the nth iteration is to find the nth least number in the right half of the array.
        The Min loop within the outer loop determines the next least number and swaps it with the nth index in main array.
        Moves the iteration index ahead, making the array split into three parts again.

        Termination:
        Algorithm terminates when the index has sorted last but one element in the array.
        As the last element will be the least in the remaining list, which is itself.
    """
    for i in range(0, len(A)-1):
        min_val=A[i]
        min_idx = i
        j=i+1
        while j<len(A):
            if A[j]<min_val:
                min_val = A[j]
                min_idx = j
            j=j+1
        temp = A[i]
        A[i] = A[min_idx]
        A[min_idx] = temp
    return A

