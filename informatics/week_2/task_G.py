import sys


def dfs(graph, edge_from, edge_to, start, enter, reach, parent, parent_edge, ans_from, ans_to):
    time = 1
    stack = [[start, 0]]
    enter[start] = reach[start] = time
    time += 1
    while stack:
        v, idx = stack[-1]
        if idx == len(graph[v]):
            stack.pop()
            if parent[v] != -1:
                p = parent[v]
                reach[p] = min(reach[p], reach[v])
                if reach[v] > enter[p]:
                    return False
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
                ans_from[edge_idx] = v
                ans_to[edge_idx] = w
                enter[w] = reach[w] = time
                time += 1
                parent[w] = v
                parent_edge[w] = edge_idx
                stack.append([w, 0])
            else:
                reach[v] = min(reach[v], enter[w])
                if ans_from[edge_idx] == -1:
                    ans_from[edge_idx] = v
                    ans_to[edge_idx] = w
    return True


if __name__ == '__main__':
    n = int(sys.stdin.buffer.readline())
    m = int(sys.stdin.buffer.readline())
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
    ans_from = [-1] * m
    ans_to = [-1] * m
    possible = True
    for i in range(n):
        if enter[i] == 0:
            if not dfs(graph, edge_from, edge_to, i, enter, reach, parent, parent_edge, ans_from, ans_to):
                possible = False
                break
    if not possible:
        print(0)
    else:
        for i in range(m):
            print(f'{ans_from[i] + 1} {ans_to[i] + 1}')
