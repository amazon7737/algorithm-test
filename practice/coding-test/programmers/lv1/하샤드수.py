def solution(x):
    b = str(x);c = 0
    print(x)
    for i in range(len(b)):
        c += int(b[i])
    if (x % c) == 0:
        return True
    return False
    print(c)    
