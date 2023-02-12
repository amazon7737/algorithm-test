def solution(i, j, k):
    cnt=0
    for l in range(i,j+1):
        str_l=list(str(l))
        str_k=str(k)
        if str_k in str_l:
            cnt+=str_l.count(str_k)
    return cnt


    # 11 에서 2번 1이 체크되는 반례를 찾기못함.
