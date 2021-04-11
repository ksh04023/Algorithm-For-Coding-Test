#팩토리얼

N = int(input())

def factorial(num):
    global answer
    if num == 0 :
        return 1
    else:
        return num*factorial(num-1)
# 재귀함수 만들때
# - 종료조건 입력
# - return 할때 다음 차례에서 필요한 값을 리턴하도록


answer = 1
answer = factorial(N)

print(answer)