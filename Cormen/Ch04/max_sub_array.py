"""
Given an array of elements find the sub-array which has the largest sum of the entire array.

E.g.
Given ticker values of a stock at end of day for future in advance to trader,
Can the trader decide to find which day to buy and which day to sell the stock on ?


Ticker values : [100,113,110,85,105,102,86,63,81,101,94,106, 101, 79, 94, 90, 97]

deltas : [-, 13,-3,-15,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

Given the difference array which calculates the difference of stock value to its previous day, barring the first ticker value.
Find the maximum-sub-array i.e. day which trader can buy the stock and sell it making maximum profit of the given future ticker values.

Brute force algorithm :
    is to find sum of any two of the N values and find the largest.
    Solution has a run time of O(N^2)

divide-and-conquer :
    1) split the array into two :
    2) find the max value in left sub-array and right sub-array independently
    3) find the max value between min index of left-sub-array and max index of right-sub-array.
    4) compare max-left, max-right and max-crossing-mid to find the max value.

"""


def find_max_crossing_subarray(low, mid, high, A):
    '''
    Combine method of the divide-and-conquer algorithm

    :param A:  Array of integers
    :param low: left low found by d&c left split.
    :param mid:  split point of Array.
    :param high: right high found by d&c right split.
    :return:  returns low, high, max.
    '''

    left_sum = right_sum = float('-inf')
    max_left = max_right = mid
    sum = 0
    for i in range(mid,low-1,-1):
        sum = sum + A[i]
        if sum > left_sum :
            left_sum = sum
            max_left = i
    sum = 0
    for j in range(mid+1, high+1, 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)



def find_max_subarray(low, high, A):
    'Base case of one element in the Array'
    if high == low :
        return (low, high, A[low])

    'Dividing the problem in two sub-problems.'
    mid = (int)((low+high) / 2)
    (left_low, left_high, left_sum ) = find_max_subarray(low, mid, A)
    (right_low, right_high, right_sum) = find_max_subarray(mid+1, high, A)

    'Combine phase of divide-and-conquer'
    (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(low, mid, high, A)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    if right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    return (cross_low, cross_high, cross_sum)


def find_max_subarray_brute_force(low, high, A):
    max_sum = float('-inf')
    st_idx = 0
    end_idx = 0
    for i in range(low, high):
        sum = A[i]
        for j in range(i+1, high):
            sum = sum + A[j]
            if sum > max_sum:
                max_sum = sum
                st_idx = i
                end_idx = j
    return st_idx,end_idx,max_sum

def linear_max_subarray_solution(A):
    m_seq = 0
    m_max = float('-inf')
    max_low = 0
    max_high = 0
    max_st = 0

    for i in range(0,len(A),1):
        m_seq += A[i]
        if m_seq > m_max:
            max_low = max_st
            max_high = i
            m_max = m_seq
        if m_seq < 0:
            m_seq = 0
            max_st = i+1
    return max_low, max_high, m_max




