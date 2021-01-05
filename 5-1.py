# 음료수 얼려 먹기

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

answer = 0

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False


for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer += 1

print(answer)