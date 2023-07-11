def solution(s):
    arr = list(s.split(" ")); arr2 = []; a= 0; b=0
    for i in range(len(arr)-1, -1, -1):
        arr2.append(arr[i])
    print(arr2)    
    
    for i in range(len(arr2)):
        try:
            b = int(arr2.pop())
            a += b
            
        except ValueError:
            a -= b
            
    return a
