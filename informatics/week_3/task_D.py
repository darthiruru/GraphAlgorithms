import sys


def get_mst(buckets, n):
    res = 0
    cnt = 0
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(x, y):
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
    for w in range(10001):
        for p in buckets[w]:
            x = find(p // n)
            y = find(p % n)
            if x != y:
                res = w
                union(x, y)
                cnt += 1
                if cnt == n - 1:
                    return res
    return res


if __name__ == '__main__':
    n, k = map(int, sys.stdin.buffer.readline(). split())
    buckets = [[] for _ in range(10001)]
    for _ in range(k):
        x, y, w = map(int, sys.stdin.buffer.readline().split())
        x -= 1
        y -= 1
        buckets[w].append(x * n + y)
    print(get_mst(buckets, n))
