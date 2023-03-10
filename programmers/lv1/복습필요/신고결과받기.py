from collections import defaultdict
# dict 딕셔너리에 추가하는 기능을 사용할때는 defaultdict 사용하면됨.

def solution(id_list, report, k):
    # 한번에 한명의 유저를 신고할 수 있음.
    # 한 유저를 여러 번 신고할 수 있음, 동일한 유저에 대한 신고 횟수는 1회로 처리
    # k번 이상 신고된 유저는 게시판 이용 정지 , 메일을 발송
    # k = 2 , 2번 이상 신고당하면 이용 정지
    
    # 중복신고 제거
    report = list(set(report))
    # 
    # 신고당한 애들
    user = defaultdict(set)
    # 누적 횟수
    cnt = defaultdict(int)
    
    # 통보메일 보내는 애들
    for i in report:
        a, b = i.split()
       #print(a, b)
        user[a].add(b)
        cnt[b]+=1
        
    arr=[]    
    for j in id_list:
        answer =0
        for u in user[j]:
            if cnt[u]>=k:
                answer += 1
        arr.append(answer)        
   #print("arr:",arr)    
        
    return arr    
