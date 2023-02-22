def solution(k, m, score):
    # 최대 점수 k , 한상자에 들어가는 사과수 m, 사과들의 점수 score
    # ? : 과일 장수가 얻을 수 있는 최대 이익
    score.sort(reverse = True)
    # m = 4
    cnt = 0;answer=0
    for i in range(0, len(score), m):
        cnt = score[i:i+m]
        print("cnt:", cnt)
        if len(cnt) == m:
            # 최저 사과 점수 X 한 상자에 담긴 사과 개수 X 상자의 개수( 상자가 1개라고 가정했을때)
            answer += min(cnt) *m # 개수 자체가 되는거다
            
    return answer        
