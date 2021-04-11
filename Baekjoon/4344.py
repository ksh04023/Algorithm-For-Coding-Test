#평균은 넘겠지

C = int(input())

data = []
data_size = []
for _ in range(C):
    input_temp = list(map(int,input().split()))
    data_size.append(input_temp[0])
    data.append(input_temp[1:])

print(data)

for i in range(C):
    temp_data = data[i]
    sum = 0
    count = 0
    for j in temp_data:
        sum += j

    avg = sum/len(temp_data)

    for k in temp_data:
        if k > avg:
            count += 1

    print(count)
    ratio = count/data_size[i]*100
    ratio = round(ratio,3)
    print(str(ratio) + '%')
    

