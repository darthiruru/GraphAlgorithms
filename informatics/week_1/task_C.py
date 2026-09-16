def get_path(graph, n):
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                cur_dist = graph[i][j] + graph[j][k] + graph[k][i]
                if cur_dist < min_dist:
                    path = (i+1, j+1, k+1)
                    min_dist = cur_dist
    return path

if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(*get_path(graph, n))