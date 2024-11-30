
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
def longestDiverseString(a:int, b:int, c:int)->str:
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
def maximumSwap(num:int)->int:
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

"""
No.62
There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner 
(i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths 
that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109
"""
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m == 1 or n == 1:
        return 1
    l_edge = max(m, n)
    s_edge = min(m, n)
    res = [[0] * l_edge]
    for i in range(l_edge - 1):
        res.append([0] * (l_edge+1))
    for i in range(l_edge):
        res[i][0] = 1
        sum = 1
        for j in range(1, i+1):
            res[i][j] = res[i-1][j] + res[i][j-1]
            sum += res[i][j]
            if i >= l_edge-1 and j >= s_edge-1:
                return res[l_edge - 1][s_edge - 1]
        res[i][i+1] = sum
    # Sm,n = Sm,n-1 + Sm-1,n-1 + ... + Sn-1,n-1 + Sn-1,n-2 + ... + Sn-1,1
    # Sm,n = Sm,n-1 + Sm-1,n
    return res[l_edge - 1][s_edge - 1]

print(uniquePaths(7,3))
