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
