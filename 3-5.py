arr = list(map(int,input().split()))

arr.sort()
answer = 0

while True:
    a = arr[-1]
    arr.remove(a)

    if len(arr) >= a-1:
        answer += 1
        for i in range(a-1):
            arr.remove(arr[i])
    else:
        break

    if len(arr) == 0:
        break

print(answer)

    