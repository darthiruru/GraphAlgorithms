def count_roads(roads, n):
    ans = sum([sum(row) for row in roads]) / 2
    return int(ans)

if __name__ == '__main__':
    n = int(input())
    roads = [list(map(int, input().split())) for _ in range(n)]
    print(count_roads(roads, n))