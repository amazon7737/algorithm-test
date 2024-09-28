def solution(s):
    b=''
    a = round(len(s)//2)
    if len(s) % 2 ==0:
            b+=s[a-1];b+=s[a]
            return b
    else:
        return s[a]
