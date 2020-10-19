

def linear_search(A, key):
    index = None
    for i in range(1,len(A)):
        if key == A[i]:
            index = i+1
    return index