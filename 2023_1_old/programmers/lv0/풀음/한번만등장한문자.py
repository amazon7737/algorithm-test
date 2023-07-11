
def solution(s):
    # s 한번만 등장하는 숫자 -> 사전순 정렬

    arr = [] ; arr2 = []; arr3 = []
    a = ''
    for j in range(len(s)):
        arr.append(s[j])
    arr.sort()
    print("arr: ", arr)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if arr[i] == arr[j]:
                arr2.append(arr[i])
    print("arr2: ", arr2)
    for i in range(len(s)):
        if arr[i] not in arr2:
            arr3.append(arr[i])
    print("arr3: ", arr3)

    for i in range(len(arr3)):
        a += arr3[i]

    return a
