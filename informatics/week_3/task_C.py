def get_mst(coords, segments):
    res = 0
    n = len(coords)
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

    for x, y in segments:
        union(find(x), find(y))

    edges = []
    for x in range(n):
        for y in range(x + 1, n):
            if [x, y] not in segments:
                w = ((coords[x][0] - coords[y][0]) ** 2 +
                     (coords[x][1] - coords[y][1]) ** 2) ** 0.5
                edges.append([w, x, y])
    edges.sort()
    for w, x, y in edges:
        x = find(x)
        y = find(y)
        if x != y:
            res += w
            union(x, y)
    return res


if __name__ == '__main__':
    n = int(input())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append([x, y])
    m = int(input())
    segments = []
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        segments.append([min(a, b), max(a, b)])
    print(f'{get_mst(coords, segments):.5f}')
