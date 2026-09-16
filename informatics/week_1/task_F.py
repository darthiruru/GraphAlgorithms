def is_tree(graph, v, e):
    visited = {0}
    queue = [0]
    while queue:
        x = queue.pop()
        for y in graph[x]:
            if y not in visited:
                queue.append(y)
                visited.add(y)
    if len(visited) != v or v != e + 1:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    n = int(input())
    graph = {i: [] for i in range(n)}
    num_edges = 0
    for j in range(n):
        for i, elem in enumerate(input().split()):
            if int(elem) == 1:
                graph[i].append(j)
                num_edges += 1
    print(is_tree(graph, n, num_edges // 2))
