import sys
from heapq import heappush, heappop

n = int(input())
m = int(input())

city = [[] for _ in range(n+1)]
value = [float('inf') for _ in range(n+1)]

for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    city[start].append([end, weight])

start_city, end_city = map(int, input().split())

def dijkstra(start_city):
    # 내장 모듈인 heapq는 최소 힙으로 만들어짐
    # 그래서 pop을 하면 최소값이 반환됨
    value[start_city] = 0
    heap = []
    heappush(heap, [0, start_city])

    while heap:
        now_value, now_edge = heappop(heap)

        if now_value > value[now_edge]:
            continue

        for edge, weight in city[now_edge]:
            new_weight = now_value + weight

            if new_weight < value[edge]:
                value[edge] = new_weight
                heappush(heap, [new_weight, edge])

dijkstra(start_city)
print(value[end_city])