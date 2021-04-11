#성적이 낮은 순서로 학생 출력하기

N = int(input())

data = []
for _ in range(N):
    str = input().split()
    data.append((str[0], int(str[1])))

data = sorted(data, key=lambda student: student[1])

for student in data:
    print(student[0], end=' ')
