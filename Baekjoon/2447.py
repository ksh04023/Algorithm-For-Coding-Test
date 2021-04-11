#별찍기 - 10

N = int(input())

def blank(stars, n){
    if n < 3:
        return

    for i in range(start, end):
        for k in range(start, end):
            stars[i][k] = ''
    
    a = n/3 #indexing 할 숫자
    count = n/a
    c = 0
    for p in range(n):
        if n%p == 0:
            start = c * a
            end = (c+1) * a
            c += 1
            blank(start,)
}

stars = ['*'*N for _ in range(N)]

n = N
blank(stars,n)