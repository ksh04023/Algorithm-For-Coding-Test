#피보나치

n = int(input())

pibo = [0,1]
for i in range(n+1):
    if i < 2:
        continue
    else:
        num = pibo[-1] + pibo[-2]
        print(num)
        pibo.append(num)

print(pibo[n])
