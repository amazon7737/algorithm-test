# 미친 1줄

solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

# 해설 !

def solution(a, b, n):
    cnt = 0

    while n >= a:
        c = n // a
        n = n - (a *c) + (c * b)
        cnt += c*b
    return cnt
