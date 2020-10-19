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
    """Sorts a list of integers in ascending or descending order.

        Parameters
        ----------
        A : list
            List of integers to be sorted.
        order : 0,1
            0 is ascending order
            1 is descending order.

        Returns
        -------
        list
            a list of sorted integers in the specified order.


        Complexity
        ----------

        Best Case : O(n)
        Worst Case : O(n^2)

        """
    if order == 0:
        return _insertion_sort_asc(A)
    elif order == 1:
        return _insertion_sort_desc(A)