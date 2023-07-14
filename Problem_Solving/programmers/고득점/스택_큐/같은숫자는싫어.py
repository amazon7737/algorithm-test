def solution(arr):
    ch = []
    ch.append(arr[0])
    for i in range(1, len(arr)):
        if ch[-1] == arr[i]:
            pass
        else:
            ch.append(arr[i])
    return ch     
