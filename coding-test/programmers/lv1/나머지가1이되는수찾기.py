def solution(n):
    arr = []
    for i in range(1, n):
        if n % i == 1:
            arr.append(i)
    return min(arr)
