def solution(my_string):
    arr2 = [] ; a=0
    
    
    
    arr = list((my_string).split(" "))
    a += int(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == "+":
            a += int(arr[i+1])
        elif arr[i] == "-":
            a -= int(arr[i+1])
    print(a)    
    print(arr)
    
    return a
