import heapq


def get_mst(graph, weights, n):
    res = 0
    best = [float('inf') for _ in range(n)]
    best[0] = 0
    heap = [(0, 0)]
    used = [False] * n
    while heap:
        w, u = heapq.heappop(heap)
        if used[u]:
            continue
        used[u] = True
        res += w
        for v in graph[u]:
            if not used[v] and weights[(min(v, u), max(v, u))] < best[v]:
                best[v] = weights[(min(v, u), max(v, u))]
                heapq.heappush(heap, (best[v], v))
    return res


if __name__ == '__main__':
    n, m = map(int, input(). split())
    graph = [[] for _ in range(n)]
    weights = dict()
    for _ in range(m):
        x, y, w = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
        weights[(min(x, y), max(x, y))] = w
    print(get_mst(graph, weights, n))
