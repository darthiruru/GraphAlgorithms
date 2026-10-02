def dfs(graph, start, color, tree):
    color[start] = 1
    for v in graph[start]:
        if color[v] == 0:
            tree.append((start + 1, v + 1))
            dfs(graph, v, color, tree)


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
    tree = []
    color = [0] * n
    dfs(graph, 0, color, tree)
    for edge in tree:
        print(*edge)
