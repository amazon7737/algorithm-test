from collections import deque
import itertools
import math
def solution(nums):
    a = itertools.combinations(nums, 3)
    
    arr = list(a); arr2=[];arr3=[]
    for i in range(len(arr)):
        arr2.append(sum(arr[i]))
    print(arr2)    
    for j in range(len(arr2)):
        if isPrime(arr2[j]) == True:
            arr3.append(arr2[j])
    print(arr3)
    return len(arr3)
def isPrime(n):
    # 1, 2 예외
    if n <= 1:
        return False
    if n == 2:
        return True
    
    
    # 2 이외의 짝수는 모두 소수가 아님
    if n % 2 == 0:
        return False
    
    # 3부터 판단
    sqrtn = int(math.sqrt(n))
    for div in range(3, sqrtn+1, 2):
        if n % div == 0:
            return False
        
    return True    
