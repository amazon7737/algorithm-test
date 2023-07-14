import math
# 최소공배수 : 두수곱 // 최대공약수(두수)
# 계속 앞에수부터 대입하면서 돌리면 N개의 최소공배수
def solution(arr):
    number = arr[0]
    
    for num in arr:
        number = number* num // math.gcd(number, num)
    return number

