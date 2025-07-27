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

"""
No.1233
你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。
folder[j] 的子文件夹必须以 folder[j] 开头，后跟一个 "/"。例如，"/a/b" 是 "/a" 的一个子文件夹，但 "/b" 不是 "/a/b/c" 的一个子文件夹。
文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。
例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。
"""
def removeSubfolders(folder):
    """
    :type folder: List[str]
    :rtype: List[str]
    """
    class Trie:
        def __init__(self):
            self.children = dict()
            self.ref = -1
    
    root = Trie()
    for i in range(len(folder)):
        dir_name = folder[i].split("/")
        current_node = root
        for j in range(len(dir_name)):
            if dir_name[j] not in current_node.children:
                # 中间节点的ref保持为-1
                current_node.children.update({dir_name[j]: Trie()})
            current_node = current_node.children[dir_name[j]]
        # current_node是最深的目录节点,ref等于其在folder中的索引
        current_node.ref = i
    # 最后构造出的树结构中,在folder中出现过的目录节点,ref为它在folder中的索引
    # folder中没出现的中间节点,其ref值为-1
    
    result = []
    def dfs(trie):
        if trie.ref == -1:
            # 说明该节点未在原始folder中出现过,所以继续搜索其子节点
            for child in trie.children.values():
                dfs(child)
        else:
            # 说明该节点在原始folder中存在,ref为它在folder中的索引,并且其所有祖先节点都未在folder中出现
            # 该节点的所有孩子节点都是它的子目录,不需要出现在结果中,因此停止搜索直接return
            result.append(folder[trie.ref])
            return
    dfs(root)
    return result
    

if __name__ == '__main__':
    pass
