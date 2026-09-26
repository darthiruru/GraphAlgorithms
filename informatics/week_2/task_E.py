import sys


def dfs(graph, start, visited, order, idx):
    visited[start] = 1
    stack = [start]
    while stack:
        v = stack[-1]
        if idx[v] < len(graph[v]):
            w = graph[v][idx[v]]
            idx[v] += 1
            if not visited[w]:
                visited[w] = 1
                stack.append(w)
        else:
            stack.pop()
            order.append(v)


def dfs_(graph, start, components, component_id):
    components[start] = component_id
    stack = [start]
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if not components[w]:
                components[w] = component_id
                stack.append(w)


def strongly_connected_components(graph, graph_, components, n):
    visited = [0] * n
    idx = [0] * n
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, order, idx)
    count = 0
    for i in reversed(order):
        if components[i] == 0:
            count += 1
            dfs_(graph_, i, components, count)
    return count


if __name__ == '__main__':
    n, m = map(int, sys.stdin.buffer.readline().split())
    graph = [[] for _ in range(n)]
    graph_ = [[] for _ in range(n)]
    for _ in range(m):
        v, w = map(int, sys.stdin.buffer.readline().split())
        v -= 1
        w -= 1
        graph[v].append(w)
        graph_[w].append(v)
    components = [0] * n
    count = strongly_connected_components(graph, graph_, components, n)
    print(count)
    print(*components)
