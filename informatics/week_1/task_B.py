def count_traffic_lights(traffic_lights,m, n):
    res = [0] * n
    for i in range(m):
        res[traffic_lights[i][0] - 1] += 1
        res[traffic_lights[i][1] - 1] += 1
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    traffic_lights = [list(map(int, input().split())) for _ in range(m)]
    print(*count_traffic_lights(traffic_lights, m, n))