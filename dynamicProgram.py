
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
