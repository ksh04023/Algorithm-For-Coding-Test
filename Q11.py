#뱀
import sys
input = sys.stdin.readline

n = int(input()) #보드 크기
k = int(input()) #사과 개수

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    a, b = map(int,input().split())
    board[a][b] = 1 #사과의 위치

dir = []
dir_count = int(input())
for i in range(dir_count):
    x,c = input().split()
    dir.append([int(x),c])

dx = [1, 0, -1, 0] #우, 상, 좌, 하
dy = [0, -1, 0, 1]
sec = 0
length = 1
x=1
y=1
bam = [[1,1]]
cur_dir = 0 #오른쪽:-1, 왼쪽: 1
next_dir = dir[0]

while True:
    sec += 1
    x = x + dx[cur_dir]
    y = y + dy[cur_dir]
    print(x, y)
    if x < 1 or y < 1 or x > n or y > n:
        break
    if (x,y) in bam:
        print(x, y)
        break
    if board[x][y] != 1: #사과 아니면
        tail = bam[0]
        bam.remove(bam[0])
        board[tail[0]][tail[1]] = 0
    

    print(next_dir)
    if sec == next_dir[0]:
        if next_dir[1] == 'L':
            cur_dir += 1
        else:
            cur_dir -= 1
        dir.remove(dir[0])
        next_dir=dir[0]
    


    bam.append([x,y])

print(sec)
    


    



