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


"""
No.1405
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
"""
def longestDiverseString(self, a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: str
    """
    result_str = ''
    list_abc = [[a, 'a', 'aa'], [b, 'b', 'bb'], [c, 'c', 'cc']]
    list_abc.sort(reverse=True)
    max_letter = list_abc[0]
    middle_letter = list_abc[1]
    min_letter = list_abc[2]
    #use a mathematical function to solve this problem
    if max_letter[0] >= 2 * (min_letter[0] + middle_letter[0]):
        result_str += (max_letter[2] + min_letter[1]) * min_letter[0]
        result_str += (max_letter[2] + middle_letter[1]) * middle_letter[0]
        if max_letter[0] - 2 * (min_letter[0] + middle_letter[0]) >= 2:
            result_str += max_letter[2]
        elif max_letter[0] - 2 * (min_letter[0] + middle_letter[0]) == 1:
            result_str += max_letter[1]
    elif min_letter[0] + middle_letter[0] < max_letter[0] < 2 * (min_letter[0] + middle_letter[0]):
        difference = max_letter[0] - middle_letter[0] - min_letter[0]
        if difference > middle_letter[0]:
            result_str += (max_letter[2] + middle_letter[1]) * middle_letter[0]
            result_str += (max_letter[2] + min_letter[1]) * (difference - middle_letter[0])
            result_str += (max_letter[1] + min_letter[1]) * (min_letter[0] + middle_letter[0] - difference)
        elif difference <= middle_letter[0]:
            result_str += (max_letter[2] + middle_letter[1]) * difference
            result_str += (max_letter[1] + middle_letter[1]) * (middle_letter[0] - difference)
            result_str += (max_letter[1] + min_letter[1]) * min_letter[0]
    elif max_letter[0] <= min_letter[0] + middle_letter[0]:
        result_str += (max_letter[1] + middle_letter[1] + min_letter[1]) * (middle_letter[0] + min_letter[0] - max_letter[0])
        result_str += (max_letter[1] + min_letter[1]) * (max_letter[0] - middle_letter[0])
        result_str += (max_letter[1] + middle_letter[1]) * (max_letter[0] - min_letter[0])
    return result_str


"""
No.670
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.
"""
def maximumSwap(num):
    """
    :type num: int
    :rtype: int
    """
    sorted_num = sorted(str(num), reverse=True)
    original_num = list(str(num))
    index = 0
    for i in range(len(original_num)):
        if original_num[i] != sorted_num[i]:
            index = i
            break
    max_index = index
    current_max = original_num[index]
    for i in range(index, len(original_num)):
        if original_num[i] >= current_max:
            current_max = original_num[i]
            max_index = i
    original_num[max_index], original_num[index] = original_num[index], original_num[max_index]
    return int(''.join(original_num))
