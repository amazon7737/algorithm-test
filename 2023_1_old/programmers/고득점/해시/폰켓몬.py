# 폰켓몬 ( 프로그래머스)


def solution(nums):
    answer = 0
    n = len(nums) // 2
    arr = list(set(nums))

    for i in arr:
        if answer < n:
            answer += 1
        print(i)
    return answer






