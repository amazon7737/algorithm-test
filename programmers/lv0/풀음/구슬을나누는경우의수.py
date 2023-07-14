def solution(balls, share):
    # a : n , b : m , c : n - m
    a = 1; b = 1; c = 1
    for i in range(balls, 0, -1):
        a *= i
    for j in range(share, 0, -1):
        b *= j
    for k in range(balls-share, 0 , -1):
        c *= k
    return a//(c*b)
