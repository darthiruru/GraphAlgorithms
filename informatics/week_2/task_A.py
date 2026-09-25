from collections import deque


def find_optimal_path(n, x1, y1, x2, y2):
    graph = dict()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            v = (i, j)
            if i - 2 > 0 and j - 1 > 0:
                graph.setdefault(v, set()).add((i-2, j-1))
                graph.setdefault((i-2, j-1), set()).add(v)
            if i - 1 > 0 and j - 2 > 0:
                graph.setdefault(v, set()).add((i-1, j-2))
                graph.setdefault((i-1, j-2), set()).add(v)
            if i + 1 <= n and j - 2 > 0:
                graph.setdefault(v, set()).add((i+1, j-2))
                graph.setdefault((i+1, j-2), set()).add(v)
            if i + 2 <= n and j - 1 > 0:
                graph.setdefault(v, set()).add((i+2, j-1))
                graph.setdefault((i+2, j-1), set()).add(v)
            if i + 2 <= n and j + 1 <= n:
                graph.setdefault(v, set()).add((i+2, j+1))
                graph.setdefault((i+2, j+1), set()).add(v)
            if i + 1 <= n and j + 2 <= n:
                graph.setdefault(v, set()).add((i+1, j+2))
                graph.setdefault((i+1, j+2), set()).add(v)
            if i - 1 > 0 and j + 2 <= n:
                graph.setdefault(v, set()).add((i-1, j+2))
                graph.setdefault((i-1, j+2), set()).add(v)
            if i - 2 > 0 and j + 1 <= n:
                graph.setdefault(v, set()).add((i-2, j+1))
                graph.setdefault((i-2, j+1), set()).add(v)
    Q = deque()
    Q.append((x1, y1))
    visited = {v: 0 for v in graph}
    visited[(x1, y1)] = 1
    prev_node = {(x1, y1): None}
    flag = False
    while Q:
        v = Q.popleft()
        for w in graph[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1
                prev_node[w] = v
                if w == (x2, y2):
                    flag = True
        if flag:
            break
    start = (x2, y2)
    path = [(x2, y2)]
    while prev_node[start]:
        path.append(prev_node[start])
        start = prev_node[start]
    print(len(path) - 1)
    for node in path[::-1]:
        print(*node)


if __name__ == '__main__':
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    find_optimal_path(n, x1, y1, x2, y2)
