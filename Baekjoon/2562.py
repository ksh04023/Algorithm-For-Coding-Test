#최댓값

data = []
for _ in range(9):
    data.append(int(input()))

a = max(data)
print(a)
print(data.index(a)+1)