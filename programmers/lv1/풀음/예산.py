def solution(d, budget):
    cnt = 0
    d.sort()
    for i in range(len(d)):
        if budget - d[i] >= 0:
            budget -= d[i]
            cnt += 1
    return cnt
