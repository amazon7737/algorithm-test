# k번째수 프로그래머스 , 고득점 kit 정렬

def solution(array, commands):

    y = 0
    arr3 = []
    for x in range(len(commands)):
        i = commands[x][y]
        j = commands[x][y+1]
        k = commands[x][y+2]

        arr2 = array[i-1:j]
        arr2_ = sorted(arr2)
        arr3.append(arr2_[k-1])
    return arr3

