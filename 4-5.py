#문자열 재정렬

string = input()
str_list = [e for e in string]

num_list = []
char_list = []

for ch in str_list:
    try:
        num = int(ch)
        num_list.append(num)
    except:
        char_list.append(ch)

sum_num = sum(num_list)
char_list.sort()
answer = ''.join(char_list)
answer += str(sum_num)
print(answer)