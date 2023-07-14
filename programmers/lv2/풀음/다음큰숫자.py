def solution(n):
    arr = []
    for i in range(10):
        arr.append(str(bin(n+i)))
    for i in range(1,len(arr)):
        if arr[0].count('1') == arr[i].count('1'):
            return int(arr[i],2)
