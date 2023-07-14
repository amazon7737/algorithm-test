
def solution(n):
    arr = []
    a = 1
    for i in range(1, 11):
        a = a * i
        arr.append(a)
    print(arr)
    for j in range(len(arr)):
        try:
            if arr[j] <= n and arr[j+1] > n:
                return arr.index(arr[j])+1
        except IndexError:
            return arr.index(arr[j])+1
