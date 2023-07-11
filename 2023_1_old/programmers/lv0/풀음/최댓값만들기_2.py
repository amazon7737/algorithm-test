def solution(numbers):
    arr = []
    for i in range(len(numbers)):
        for j in range(i):
            arr.append(numbers[i]*numbers[j])
    return max(arr)
