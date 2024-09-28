def solution(price, money, count):
    a = 0
    for i in range(price, price*count+1, price):
        a += i
    if a - money <= 0:
        return 0
    return a - money
