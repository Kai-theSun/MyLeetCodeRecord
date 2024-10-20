import heapq
import math
from collections import deque
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
def parseBoolExpr(expression):
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
