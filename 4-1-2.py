n = int(input())
data = input().split()

moves = ['R','L','U','D']

dx = [0,0,-1,1]
dy = [1,-1,0,0]

x=1
y=1

for direction in data:
    for i in range(len(moves)):
        if direction == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx <1 or ny <1 or nx>5 or ny>5:
        continue

    x, y = nx, ny

print(x,y)