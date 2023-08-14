def solution(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i]*b[i]
    return c    
# 2023.08.11 
def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])
