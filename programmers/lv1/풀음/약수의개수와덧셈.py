def solution(left, right):
    arr = [];arr.append(1); number=0
    for j in range(left, right+1):
        cnt = 0
        for i in range(1, j+1):
            if i in arr:
                pass
            elif j % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            number += j
        else:
            number -= j
    print(cnt)
    return -1*number
