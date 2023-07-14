def solution(n):
    arr=  list(str(n));arr2= []
    for i in range(len(arr)):
        arr2.append(int(arr[i]))
    arr2.sort(reverse = True)    
    a = ''
    for i in range(len(arr2)):
        a += str(arr2[i])
    return int(a)
