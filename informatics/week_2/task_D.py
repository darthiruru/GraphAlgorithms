import sys


def dfs(graph, edge_from, edge_to, start, enter, reach, parent, parent_edge):
    time = 1
    stack = [[start, 0]]
    bridges = []
    enter[start] = reach[start] = time
    time += 1
    while stack:
        v, idx = stack[-1]
        if idx == len(graph[v]):
            stack.pop()
            if parent[v] != -1:
                reach[parent[v]] = min(reach[parent[v]], reach[v])
                if reach[v] > enter[parent[v]]:
                    bridges.append(parent_edge[v] + 1)
        else:
            stack[-1][1] += 1
            edge_idx = graph[v][idx]
            if edge_from[edge_idx] == v:
                w = edge_to[edge_idx]
            else:
                w = edge_from[edge_idx]
            if edge_idx == parent_edge[v]:
                continue
            if enter[w] == 0:
                enter[w] = reach[w] = time
                parent[w] = v
                parent_edge[w] = edge_idx
                time += 1
                stack.append([w,  0])
            else:
                reach[v] = min(reach[v], enter[w])
    return bridges


if __name__ == '__main__':
    n, m = map(int, sys.stdin.buffer.readline().split())
    graph = [[] for _ in range(n)]
    edge_from = [0] * m
    edge_to = [0] * m
    for i in range(m):
        v, w = map(int, sys.stdin.buffer.readline().split())
        v -= 1
        w -= 1
        graph[v].append(i)
        graph[w].append(i)
        edge_from[i] = v
        edge_to[i] = w
    enter = [0] * n
    reach = [0] * n
    parent = [-1] * n
    parent_edge = [-1] * n
    bridges = []
    for i in range(n):
        if enter[i] == 0:
            bridges.extend(dfs(graph, edge_from, edge_to, i, enter,
                           reach, parent, parent_edge))
    print(len(bridges))
    print(*sorted(bridges))
