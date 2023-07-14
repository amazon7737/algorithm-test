def solution(emergency):
    arr = []; arr2 = []; arr3 = []
    # arr2  -> 정렬 된 수 arr3 -> 순서
    # arr -> 정답
    arr2 = sorted(emergency)
    for i in range(len(emergency), 0, -1):
        arr3.append(i)
    for i in range(len(emergency)):
        arr.append(arr3[emergency.index(arr2[i])])
    return arr
