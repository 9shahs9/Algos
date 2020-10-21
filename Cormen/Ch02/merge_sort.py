import random

def merge_sort(A):
    """

    :param A:
    :return:

    Base condition is if the list has one element, the list is already sorted and can be returned back.

    if list is have more than 1 element, split the list into two lists
    Call merge sort on those two lists. Each merge sort returns a list, so there will be two lists returned.

    Combine the two lists into one list and return the sorted list.

    """
    if len(A) == 1:
        return A

    mid_point = int(len(A)/2)
    A1 = merge_sort(A[:mid_point])
    A2 = merge_sort(A[mid_point:])
    a1i = 0
    a2i = 0

    #Sentinel Card added to end of pile.
    A1.append(float('inf'))
    A2.append(float('inf'))

    #Combine operation:
    for i in range(len(A)):
        if A1[a1i] < A2[a2i]:
            A[i] = A1[a1i]
            a1i = a1i +1
        else:
            A[i] = A2[a2i]
            a2i = a2i + 1
        i = i+1
    return A

if __name__ == "__main__":
    A = [random.randint(1,100) for x in range(5)]
    print(A)
    result = merge_sort(A)
    print(result)
