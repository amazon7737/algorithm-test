def solution(n):
    arr = []
    print(6*2 % 4) 
    if n == 6:
        return 1
    
    for i in range(1, n+1):
        if (6*i) % n == 0:
            return i
