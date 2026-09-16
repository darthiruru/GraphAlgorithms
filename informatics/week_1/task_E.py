def paint_graph(s, graph, color):
    for i in graph[s]:
        if color[i-1] == -1:
            color[i-1] = 1 if color[s-1] == 0 else 0
            if not paint_graph(i, graph, color):
                return False
        elif color[i-1] == color[s-1]:
            return False
    return True


def is_two_table_enough(n, ban_list):
    graph = {i: [] for i in range(1, n+1)}
    for i, j in ban_list:
        graph[i].append(j)
        graph[j].append(i)
    color = [-1] * n
    for i in range(1, n+1):
        if color[i-1] == -1:
            color[i-1] = 0
            if not paint_graph(i, graph, color):
                return 'NO'
    return f'YES\n{" ".join([str(i+1) for i in range(n) if color[i] == 0])}'


if __name__ == '__main__':
    n, m = map(int, input().split())
    ban_list = [list(map(int, input().split())) for _ in range(m)]
    print(is_two_table_enough(n, ban_list))
