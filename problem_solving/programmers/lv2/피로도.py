# 재쉬함수 코드방법
# 

# k : 감소된 피로도
# cnt : 몇번 할 수 있는지
# dungeons : 배열들만큼..

#어떠한 변수를 가지고 할 것인지
# 전달 받은 피로도 / 던전 수 / 던전
answer = 0
visit = []
N = 0
def solution(k, dungeons):
    global visit, N
    N = len(dungeons)
    
    visit = [0] * len(dungeons)
    #answer = -1
    num(k, 0, dungeons)
    return answer

def num(k , cnt, dungeons):
   #  # 필요한 정보는 무엇인지?
    # 필요한 정보는 어느 순간 갱신되는지?
    global answer
    if answer < cnt:
        answer = cnt
    
    for i in range(N):
        # 어떠한 경우 실행(재귀) 되야 하는지
        if k >= dungeons[i][0] and visit[i] == 0:
            # 재귀함수 실행시 체크사항이 있는지
            visit[i] = 1

            # 재귀함수 실행시 변하는 변수값은 무엇인지
            num(k - dungeons[i][1], cnt+1, dungeons)
            # 재귀함수 종료시 변하는 변수값이 있는지 무엇인지
            visit[i] = 0


