def solution(num, k):
    a = str(num)
    b = str(k)
    if b in a:
        return (a.index(b) + 1)
    else:
        return -1
