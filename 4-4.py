#게임 개발

def next_dir(this_dir):
    if this_dir == 0: return 3
    elif this_dir == 1: return 0
    elif this_dir == 2: return 1
    elif this_dir == 3: return 2

def go_back(a,b,this_dir):
    global ocean
    global da
    global db
    if this_dir == 0: back_dir = 2
    elif this_dir == 2: back_dir = 0
    elif this_dir == 1: back_dir = 3
    elif this_dir == 3: back_dir = 1
    
    na = a + da[back_dir]
    nb = b + db[back_dir]

    if game_map[na][nb] == 1:
        ocean = True

    return na, nb
        

n, m = map(int,input().split())
a, b, d = map(int, input().split())

game_map=[]
for _ in range(n):
    game_map.append(list(map(int,input().split())))


visited = [[0]*n for _ in range(m)]
visited[a][b] = 1
da = [-1,0,1,0]
db = [0,1,0,-1]

ocean = False


while True:
    visit_count = 0

    for i in range(len(da)):
        d = next_dir(d) #3
        na = a + da[d] 
        nb = b + db[d]

        # #맵 벗어남
        # if na<0 or nb<0 or na>n-1 or nb>m-1:
        #     continue

        #바다이거나 이미 방문
        if game_map[na][nb] == 1 or visited[na][nb] == 1:
            visit_count += 1
            if visit_count == 4:
                a,b = go_back(a,b,d)
                break
            continue

        visited[na][nb] = 1
        print(f"yes {na} {nb}")
        a,b = na,nb

    if ocean == True:
        break

count = 0
for i in visited:
    for j in i:
        if j == 1:
            count += 1
print(visited)

