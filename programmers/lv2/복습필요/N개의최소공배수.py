import math
def solution(arr):
    number = arr[0]
    
    for num in arr:
        number = number* num // math.gcd(number, num)
    return number
