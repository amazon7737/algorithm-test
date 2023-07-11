def solution(n):
    arr = []
    arr.append(1)
    for i in range(1, n):
        if (n//i) not in arr and (n %i ) == 0:
            arr.append(n//i)
    arr.sort()
    return arr
