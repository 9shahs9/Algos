

def linear_search(A, key):
    """Find a key in a list of integers.

            Parameters
            ----------
            A : list
                List of integers.
            key : int


            Returns
            -------
            int
                index of the key within the list A.


            Complexity
            ----------

            Best Case : O(1)
            Worst Case : O(n)

    """
    index = None
    for i in range(1,len(A)):
        if key == A[i]:
            index = i+1
    return index