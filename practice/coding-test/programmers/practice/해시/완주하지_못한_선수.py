from collections import deque

def solution(participant, completion):
    
    result=""; completion = deque(completion)

    # 배열로 풀기
   # while len(completion) != 0:
   #     player = completion.popleft()
   #     for i in participant:
   #         if player == i:
   #             participant[participant.index(player)] = ""
   #             player = ""
                
   # for i in participant:
   #     if i != "":
   #         result += i
   # return result 
   # 효율성 테스트 실패


# 효율성 테스트 통과 , 딕셔너리 2개로 해결
    player = {};player2 = {}
    for i in participant:
        player[i] = 0
    for i in participant:
        player2[i] = 0
    for i in range(len(participant)):
        player2[participant[i]] += 1
    while len(completion) != 0:    
        win = completion.popleft()
        player[win] += 1
    participant = list(set(participant))
    for i in participant:
        if player[i] != player2[i]:
            result += i
    return result        
