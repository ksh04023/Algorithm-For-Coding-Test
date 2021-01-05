#미로 탈출
from collections import deque

def bfs(x,y):
    global distance
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
#이거는 오른쪽 아래로 가는거라서 쉬운데 만약 아니면??

for i in range(n):
    for j in range(m):
        bfs(0,0)

answer = graph[n-1][m-1]
print(answer)


