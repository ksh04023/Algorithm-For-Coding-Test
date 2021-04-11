# 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int,input().split()) #node개수, m: 간선 개수, k: 최단거리, x:출발지
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque([x])
distance = [-1]*(n+1)
print(distance)

distance[x] = 0
while q:
    now = q.popleft()
    print(now)
    for next_node in graph[now]:
        if distance[next_node] == -1:
            q.append(next_node)
            distance[next_node] = distance[now] + 1

count = 0
for idx, dis in enumerate(distance):
    if dis == k:
        print(idx)
        count += 1
if count == 0:
    print(-1)
        
