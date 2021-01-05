s = input()
answer = int(s[0])
for num in range(1,len(s)):
    if num <= 1 or answer <= 1:
        answer += num
    else:
        answer *= num
print(answer)
