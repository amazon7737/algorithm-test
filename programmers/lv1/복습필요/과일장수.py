def solution(k, m, score):
    # 최대 점수 k , 한상자에 들어가는 사과수 m, 사과들의 점수 score
    # ? : 과일 장수가 얻을 수 있는 최대 이익
    arr = [];a=0
    score.sort(reverse = True)
    print(score)
    for i in range(0, len(score), m):
        print(i)
        tmp = score[i:i+m]
        print(tmp)
        
        if len(tmp) ==  m:
            a += min(tmp) *m
    return a        
