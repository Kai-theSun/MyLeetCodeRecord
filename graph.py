"""
No.1462
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b,
and course b is a prerequisite of course c,
then course a is a prerequisite of course c.
You are also given an array queries where queries[j] = [uj, vj].
For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
Return a boolean array answer, where answer[j] is the answer to the jth query.
"""
def checkIfPrerequisiteClaude(numCourses, prerequisites, queries):
    # 创建可达性矩阵
    graph = [[False] * numCourses for _ in range(numCourses)]

    # 设置直接先修关系
    for pre, next in prerequisites:
        graph[pre][next] = True

    # Floyd-Warshall算法计算传递闭包
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

    # 直接查询结果
    return [graph[u][v] for u, v in queries]

def checkIfPrerequisiteGPT(numCourses, prerequisites, queries):
    # 初始化一个布尔矩阵，用来存储可达性
    reachable = [[False] * numCourses for _ in range(numCourses)]

    # 填充直接的先修关系
    for u, v in prerequisites:
        reachable[u][v] = True

    # 使用 Floyd-Warshall 算法构建传递闭包
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                if reachable[i][k] and reachable[k][j]:
                    reachable[i][j] = True

    # 根据 queries 判断是否有可达性
    return [reachable[u][v] for u, v in queries]

def checkIfPrerequisiteDeepSeek(numCourses, prerequisites, queries):
    # 构建邻接表和入度数组
    adj = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    prereq = [0] * numCourses  # 每个元素的二进制位表示前驱

    for a, b in prerequisites:
        adj[a].append(b)
        in_degree[b] += 1

    from collections import deque
    q = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        u = q.popleft()
        for v in adj[u]:
            # 将u的前驱和u自己添加到v的前驱集合中
            prereq[v] |= prereq[u] | (1 << u)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    res = []
    for u, v in queries:
        res.append((prereq[v] & (1 << u)) != 0)
    return res