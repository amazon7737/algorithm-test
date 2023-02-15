def solution(number):
    cnt = 0
    number.sort()
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] +number[k]== 0:
                    cnt += 1
                    print(number[i], number[j], number[k])
    return cnt
