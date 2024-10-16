import heapq
import math

"""
   No.2530
   You are given a 0-indexed integer array nums and an integer k. 
   You have a starting score of 0.
   In one operation:
   choose an index i such that 0 <= i < nums.length,
   increase your score by nums[i], and
   replace nums[i] with ceil(nums[i] / 3).
   Return the maximum possible score you can attain after applying exactly k operations.
"""
def maximalScore(nums, k):
    score = 0
    heap = []

    for i in range(len(nums)):
        heapq.heappush(heap, -nums[i])

    for i in range(k, 0, -1):
        tmp = -heapq.heappop(heap)
        score += tmp
        tmp = math.ceil(tmp / 3)
        heapq.heappush(heap, -tmp)

    print(type(heap))
    return score

"""
    No.632
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    :type nums: List[int]
    :rtype: int
"""
def maxSubArray(nums):
    """
    Xn : largest subarray end with nums[n]
    Xn+1 =
        if Xn < 0: nums[n+1]
        if Xn >= 0: Xn + nums[n+1]
    global_max = max(X)
    """
    max_sub_arr = nums[0]
    max_end = nums[0]
    if len(nums) == 1:
        return max_sub_arr

    for i in range(1, len(nums)):
        if max_end < 0:
            max_end = nums[i]
        else:
            max_end += nums[i]
        max_sub_arr = max(max_sub_arr, max_end)
    return max_sub_arr
