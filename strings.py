"""
No.1593
    Given a string s, return the maximum number of unique substrings
that the given string can be split into.
    You can split string s into any list of non-empty substrings,
where the concatenation of the substrings forms the original string.
    However, you must split the substrings such that all of them are unique.
    A substring is a contiguous sequence of characters within a string.
"""
"""
    :type s: str
    :rtype: int
    1 <= s.length <= 16
    s contains only lower case English letters.
"""
    # considering the maximum length of s is 16, even the O(X^n) complexity is acceptable
    # I don't understand why this question is only a Medium class
    # A complex recursion is always elegant but very hard to understood
def maxUniqueSplit(s: str) -> int:
    seen = set()
    return backtrack(s, 0, seen)

def backtrack(s, start, seen):
    if start == len(s):
        return 0
    max_count = 0

    for end in range(start + 1, len(s) + 1):
        sub_string = s[start:end]
        if sub_string not in seen:
            seen.add(sub_string)
            max_count = max(max_count, 1 + backtrack(s, end, seen))
            seen.remove(sub_string)
    return max_count


"""
No.1717
给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。
删除子字符串 "ab" 并得到 x 分。
比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
删除子字符串"ba" 并得到 y 分。
比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
请返回对 s 字符串执行上面操作若干次能得到的最大得分。
"""
def maximumGain(s, x, y):
    """
    :type s: str
    :type x: int
    :type y: int
    :rtype: int
    """
    """
    一段可以构成ab或ba的子串,能操作几次取决于a,b里较少的那个,我们希望保证能获取最高分
    因此可以先将高分组合全部删除,再进行一次相同操作删除低分组合以免遗漏
    """
    if len(s) <= 1:
        return 0
    def pop_ab(s):
        score = 0
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] == "a" and s[i] == "b":
                score += x
                stack.pop()
            else:
                stack.append(s[i])
        return score, stack
    def pop_ba(s):
        score = 0
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] == "b" and s[i] == "a":
                score += y
                stack.pop()
            else:
                stack.append(s[i])
        return score, stack
    if x >= y:
        score1, s = pop_ab(s)
        score2, s = pop_ba(s)
    else:
        score1, s = pop_ba(s)
        score2, s = pop_ab(s)
    return score1 + score2

if __name__ == '__main__':
    pass
