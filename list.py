"""
No.3487
给你一个整数数组 nums 。
你可以从数组 nums 中删除任意数量的元素，但不能将其变为 空 数组。执行删除操作后，选出 nums 中满足下述条件的一个子数组：
子数组中的所有元素 互不相同 。
最大化 子数组的元素和。
返回子数组的 最大元素和 。
子数组 是数组的一个连续、非空 的元素序列。
"""
def maxSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    if nums[-1] <= 0:
        return nums[-1]
    result = 0
    last_num = None
    for num in nums:
        if num == last_num:
            continue
        if num > 0:
            result += num
            last_num = num
    return result
    
    
if __name__ == '__main__':
    pass