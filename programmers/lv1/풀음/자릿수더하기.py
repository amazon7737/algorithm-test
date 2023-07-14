def solution(n):
    a = str(n)
    
    print(a)
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    return b
