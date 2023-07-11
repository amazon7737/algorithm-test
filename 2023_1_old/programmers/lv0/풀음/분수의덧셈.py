import math
def solution(numer1, denom1, numer2, denom2):
    up_ = (numer1 * denom2) + (numer2 * denom1) 
    down_ = (denom1 * denom2)
    if math.gcd(up_, down_) != 1:
        num = math.gcd(up_, down_)
        up_ //= num
        down_ //= num
    return [up_ , down_]
