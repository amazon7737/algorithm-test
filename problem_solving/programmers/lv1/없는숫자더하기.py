def solution(numbers):
    arr = [0,1, 2, 3,4,5,6,7,8,9];a=0
    for i in range(len(arr)):
        if arr[i] not in numbers:
            a += arr[i]
    return a     
###
# 2023.08.03(목)
def solution(numbers):
    cnt = 0
    for i in range(0, 10):
        if i not in numbers:
            cnt += i
    return cnt
