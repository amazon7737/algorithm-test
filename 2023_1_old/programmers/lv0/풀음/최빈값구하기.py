def solution(array):
    if len(array) == 1:
        return array[0]
    while len(array) != 0:
        for i in list(set(array)):
            array.remove(i)
        if len(array) == 1:
            break
    if array == []:
        return -1
    return array[0]
