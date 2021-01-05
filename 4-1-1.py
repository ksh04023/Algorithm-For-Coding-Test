n = int(input())
data = input().split()
x = 1
y = 1

for move in data:
    if move == 'R':
        if x+1 <= 5:
            x += 1
    elif move == 'L':
        if x-1 > 0:
            x -= 1
    elif move == 'U':
        if y-1 > 0:
            y -= 1
    elif move == 'D':
        if y+1 <= 5:
            y += 1

print(y,x)