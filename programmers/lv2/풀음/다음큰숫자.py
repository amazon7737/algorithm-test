def solution(n):
    arr = []
    for i in range(10):
        print(bin(n+i))
        arr.append(str(bin(n+i)))
    print("arr:",arr)
    for i in range(1,len(arr)):
        if arr[0].count('1') == arr[i].count('1'):
            return int(arr[i],2)
            
