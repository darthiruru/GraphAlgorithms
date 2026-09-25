def has_cycle(graph, start, color, path):
    color[start] = 0
    for v in graph[start]:
        if color[v] == -1:
            if has_cycle(graph, v, color, path):
                return True
        elif color[v] == 0:
            return True
    path.append(start + 1)
    color[start] = 1
    return False


def get_order(pairs, n):
    graph = {i: set() for i in range(n)}
    for pair in pairs:
        graph[pair[0] - 1].add(pair[1] - 1)
    color = [-1] * n
    path = []
    for i in range(n):
        if color[i] == -1:
            if has_cycle(graph, i, color, path):
                print('No')
                break
    else:
        print('Yes')
        print(*path[::-1])


if __name__ == '__main__':
    n, m = map(int, input().split())
    pairs = [list(map(int, input().split())) for _ in range(m)]
    get_order(pairs, n)
