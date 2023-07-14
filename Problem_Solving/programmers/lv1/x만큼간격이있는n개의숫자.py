def solution(x, n):
    arr = []
        
    if x <= 0:
        a = 1
        for _ in range(n):
            arr.append(x*a)
            a += 1
    else:        
        for i in range(x, (x*n)+1, x):
            arr.append(i)
    return arr    
    
