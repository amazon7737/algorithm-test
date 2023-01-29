def solution(numbers, direction):
    arr = []
    if direction == "right":
        a = numbers[-1]
        arr.append(numbers[-1])
        for i in range(0, len(numbers)-1):
            arr.append(numbers[i])
        return arr
    elif direction == "left":
        for i in range(1, len(numbers)):
            arr.append(numbers[i])
        
        arr.append(numbers[0])
        return arr
    print(arr)
