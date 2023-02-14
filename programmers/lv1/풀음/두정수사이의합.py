def solution(a, b):
    arr = []
    if a<b:
        for i in range(a, b+1):
            arr.append(i)
    else:        
        for i in range(a, b-1, -1):
            arr.append(i)
    return sum(arr)
