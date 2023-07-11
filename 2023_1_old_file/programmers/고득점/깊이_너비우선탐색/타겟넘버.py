# 타겟 넘버 ( 프로그래머스) 

# ** 깨달은점 : 모든 문제 상황을 경우의 수로 나누다 보면 필요한 알고리즘이 보인다.
# 각 경우의 수를 분석해서 만들어 보자.

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1

    return answer

# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS

# bfs/ dfs 사용에 대해서 잘 정리 되어 있다. 문제 상황도 잘 정리 되어있다.

# 옹알이 ( 1) (프로그래머스)

def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    count = 0
    arr2 = []
    arr2 = arr
    for i in range(len(arr)):
        for j in range(0, 4):
            arr2.append(arr[i] + arr[j])

    for i in range(len(arr)):
        for j in range(0, 4):
            arr2.append(arr2[i] + arr[j])
    for i in range(len(arr)-1, 1, -1):
        for j in range(0, 4):
            arr2.append(arr2[i] + arr[j])

    for i in range(len(babbling)):
        if babbling[i] in arr2:
            count += 1
    return count


