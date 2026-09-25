def dfs(graph, start, tin, tout):
    time = 1
    stack = [start]
    while stack:
        v = stack[-1]
        if tin[v] == 0:
            tin[v] = time
            time += 1
        if not graph[v] or tin[v] < time - 1:
            stack.pop()
            tout[v] = time
            time += 1
        else:
            for w in graph[v]:
                stack.append(w)


if __name__ == '__main__':
    n = int(input())
    parents = list(map(int, input().split()))
    tin = [0] * n
    tout = [0] * n
    graph = {i: set() for i in range(n)}
    for i in range(n):
        if parents[i] == 0:
            start = i
        else:
            graph[parents[i] - 1].add(i)
    dfs(graph, start, tin, tout)
    m = int(input())
    for _ in range(m):
        v, w = map(int, input(). split())
        if tin[v - 1] < tin[w - 1] and tout[v - 1] > tout[w - 1]:
            print(1)
        else:
            print(0)
