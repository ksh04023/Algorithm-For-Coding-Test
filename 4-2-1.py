#시간에서 '3'이 들어가는 경우의 수

N = int(input())

end_time = N * 10000 + 5959
answer = 0

for time in range(end_time):
    str_time = str(time)
    if str_time[-4:-3] > '59' or str_time[-2:-1] > '59':
        continue

    if '3' in str_time:
        answer += 1

print(answer)
