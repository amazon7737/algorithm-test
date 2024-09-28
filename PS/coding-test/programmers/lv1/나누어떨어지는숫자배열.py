def solution(arr, divisor):
    arr2 = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            arr2.append(arr[i])
    print(arr2)        
    if arr2 == []:
        arr2.append(-1)
    return sorted(arr2)
