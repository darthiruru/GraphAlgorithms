def dfs(graph, start, visited):
    visited.add(start)
    for v in range(len(graph[start])):
        if graph[start][v] == 1 and v not in visited:
            dfs(graph, v, visited)

def count_vertices(graph, start):
    visited = set()
    dfs(graph, start, visited)
    return len(visited)

if __name__ == '__main__':
    n, s = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(count_vertices(graph, s - 1))
