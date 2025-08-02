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

"""
No.2210
给你一个下标从 0 开始的整数数组 nums 。
如果两侧距 i 最近的不相等邻居的值均小于 nums[i] ，则下标 i 是 nums 中，某个峰的一部分。
类似地，如果两侧距 i 最近的不相等邻居的值均大于 nums[i] ，则下标 i 是 nums 中某个谷的一部分。
对于相邻下标 i 和 j ，如果 nums[i] == nums[j] ， 则认为这两下标属于 同一个 峰或谷。
注意，要使某个下标所做峰或谷的一部分，那么它左右两侧必须 都 存在不相等邻居。
返回 nums 中峰和谷的数量。
"""
def countHillValley(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last_num, current_num = nums[0], 0
    count = 0
    for i in range(1, len(nums)-1):
        current_num = nums[i]
        if nums[i+1] == current_num:
            continue
        if (nums[i+1] > current_num and last_num > current_num) or (nums[i+1] < current_num and last_num < current_num):
            count += 1
            last_num = current_num
    return count

"""
No.2779
给你一个下标从 0 开始的整数数组 nums 和一个 非负 整数 k 。
在一步操作中，你可以执行下述指令：
在范围 [0, nums.length - 1] 中选择一个 此前没有选过 的下标 i 。
将 nums[i] 替换为范围 [nums[i] - k, nums[i] + k] 内的任一整数。
数组的 美丽值 定义为数组中由相等元素组成的最长子序列的长度。
对数组 nums 执行上述操作任意次后，返回数组可能取得的 最大 美丽值。
注意：你 只 能对每个下标执行 一次 此操作。
数组的 子序列 定义是：经由原数组删除一些元素（也可能不删除）得到的一个新数组，且在此过程中剩余元素的顺序不发生改变。
"""
def maximumBeauty(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # 实际上转化为寻找最长的子序列,使得子序列最大值最小值之差小于2k, 滑动窗口显然是最适合的
    if len(nums) == 1:
        return 1
    nums.sort()
    left, right = 0, 0
    max_length = 0
    while left < len(nums) - max_length:
        right += 1
        while right < len(nums) and nums[right] - nums[left] > 2 * k:
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

if __name__ == '__main__':
    print(maximumBeauty([100000,100001], 9))