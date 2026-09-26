if __name__ == '__main__':
    n = int(input())
    deg = [0] * n
    for _ in range(n - 1):
        v, w = map(int, input().split())
        deg[v - 1] += 1
        deg[w - 1] += 1
    print(sum(1 if deg[i] > 1 else 0 for i in range(n)))
