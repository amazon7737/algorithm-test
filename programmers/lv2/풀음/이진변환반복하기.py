def solution(s):
    string_=''
    cnt=0 # 이진변환 횟수
    cnt2=0 # 0을 제거한 횟수
    while s != '1':
        for i in range(len(s)):
            if s[i] == '1':
                string_ += '1'
            else:
                cnt2+=1
            # len(string_) : 0 제거 후 길이
        a = bin(len(string_))
        s =a[2:]
        cnt+=1
        string_=''
    return [cnt, cnt2]  
