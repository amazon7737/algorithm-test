def solution(t, p):
    a = '';arr2= [];cnt = 0
    
    arr = list(t)
    print(arr)
    k = 0
    for _ in range(len(arr)):
        
        for i in range(k ,len(p)+k):
            
            try:
                a += arr[i]
            except IndexError:
                pass
        if len(a) != len(p):
            pass
        else:
            arr2.append(a)    
        a = ''
        k += 1  
    for i in range(len(arr2)):
        if int(arr2[i]) <= int(p):
           	cnt += 1
    return cnt
