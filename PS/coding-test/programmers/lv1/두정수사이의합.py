def solution(a, b):
    arr = []
    if a<b:
        for i in range(a, b+1):
            arr.append(i)
    else:        
        for i in range(a, b-1, -1):
            arr.append(i)
    return sum(arr)

def solution(a, b):
    if a < b :
        return sum([i for i in range(a, b+1)])
    elif a > b:
        return sum([i for i in range(b, a+1)])
    return a
