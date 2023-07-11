
#프로그래머스 : 같은숫자는 싫어

def solution(arr):
    ch = []
    ch.append(arr[0])
    for i in range(1, len(arr)):
        if ch[-1] == arr[i]:
            pass
        else:
            ch.append(arr[i])
    return ch        

# 프로그래머스 : 자릿수 더하기
def solution(n):
    arr=[]
    n = str(n)
    for i in range(len(n)):
        arr.append(int(n[i]))
    return sum(arr)


# 프로그래머스 : 짝수와 홀수
def solution(num):
    if num % 2 ==0:
        return "Even"
    else:
        return "Odd"

# 프로그래머스 : 나머지가 1이 되는 수 찾기
def solution(n):
    for i in range(1, n+1):
        if n % i == 1:
            return i

# 프로그래머스 : 약수의 합
def solution(n):
    arr=[]
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
    return sum(arr)

# 프로그래머스 : 평균 구하기
def solution(arr):
    return sum(arr)/len(arr)


# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    arr=[]
    result = x*n
    for i in range(1, n+1):
            arr.append(x*i)
    return arr
