from collections import deque
# 방문 확인을 해야하는 이유가 무엇인가 ..?
cnt = 0 ;
def solution(begin, target, words):
    words = deque(words);cnt=0
    q = begin
    
    if target not in words:
        return 0
    
    while words:
        if q == target:
            return cnt-1
        for j in range(len(words)):
            sameCnt = 0
            word = words[j]
            for i in range(len(q)):
                if q[i] != word[i]:
                    sameCnt += 1
            if sameCnt == 1:
                q = word
                cnt += 1
        print("cnt:",cnt)    
            
      
