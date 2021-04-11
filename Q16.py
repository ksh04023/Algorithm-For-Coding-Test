import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


def dfs(a,b, graph):
    if a < 0 or b < 0 or a >= n or b >= m:
        return False
    if graph[a][b] == 0:
        graph[a][b] = 2
    elif graph[a][b] == 1:
        return False
    dfs(a-1,b, graph)
    dfs(a+1,b, graph)
    dfs(a,b-1, graph)
    dfs(a,b+1, graph)

    return graph


for ax in range(n):
    for ay in range(m):
        for bx in range(n):
            for by in range(m):
                for cx in range(n):
                    for cy in range(m):
                        if (ax == bx and ay == by) or (ax == cx and ay == cy) or (cx == bx and cy == by):
                            continue
                        if graph[ax][ay] != 0 or graph[bx][by] != 0 or graph[cx][cy] != 0:
                            continue

                        copy_graph = graph.copy()

                        copy_graph[ax][ay] = 1
                        copy_graph[bx][by] = 1
                        copy_graph[cx][cy] = 1

                        for a in range(n):
                            for b in range(m):
                                if graph[a][b] == 2:
                                    dfs(a,b,copy_graph)
                        
                        
                        
                        
                        
