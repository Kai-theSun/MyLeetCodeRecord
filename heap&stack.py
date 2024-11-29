import heapq
import math
from collections import deque
from typing import List

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
def maximalScore(nums:List[int], k:int)->int:
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
No.1106
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.
"""
def parseBoolExpr(expression:str)->bool:
    """
    :type expression: str
    :rtype: bool
    1 <= expression.length <= 2 * 104
    expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
    It is guaranteed that the given expression is valid and follows the given rules.
    """
    # you should think about stack firstly when facing such calculate question with priority
    stack = deque()
    tmp = []
    for i in range(len(expression)):
        if expression[i] == ',':
            continue
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                tmp.append(stack.pop())
            stack.pop()#must be '(', and the next item must be an operator
            op = stack.pop()
            bool_res = ''
            if op == '!':
                if tmp[0] == 'f':
                    bool_res = 't'
                elif tmp[0] == 't':
                    bool_res = 'f'
            elif op == '&':
                bool_res = 't'
                for b in tmp:
                    if b == 'f':
                        bool_res = 'f'
                        break
            elif op == '|':
                bool_res = 'f'
                for b in tmp:
                    if b == 't':
                        bool_res = 't'
                        break
            stack.append(bool_res)
            tmp.clear()
        else:# be 't','f' or any operator
            stack.append(expression[i])
    result = stack.pop()
    if result == "t":
        return True
    elif result == "f":
        return False

"""
No.3254
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
Its maximum element if all of its elements are consecutive 
and sorted in ascending order, -1 otherwise.
You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1,
where results[i] is the power of nums[i..(i + k - 1)].
"""

def resultsArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == 1:
        return nums

    left_index, right_index = 0, k - 1
    newest_unsorted_index = -1
    sublist_power = []
    # use newest_unsorted_index to record an "invalid" index, which means if there exists
    # an invalid index between our left and right index, then we can judge this subarray
    # "invalid" without further calculation. On the other hand, if there is not any invalid
    # index between, we only need to compare the rightest two elements, and append the value
    # of new element if it is sorted or, append -1 if it is unsorted and renew the invalid index

    for i in range(left_index, right_index - 1):
        if nums[i + 1] != nums[i] + 1:
            newest_unsorted_index = i

    while right_index < len(nums):
        if left_index <= newest_unsorted_index:
            if nums[right_index] != nums[right_index - 1] + 1:
                newest_unsorted_index = right_index - 1
            sublist_power.append(-1)
            right_index += 1
            left_index += 1
            continue
        else:
            if nums[right_index] != nums[right_index - 1] + 1:
                newest_unsorted_index = right_index - 1
                sublist_power.append(-1)
            else:
                sublist_power.append(nums[right_index])
            right_index += 1
            left_index += 1
            continue
    return sublist_power
