from collections import deque

def bracket(s):
    arr=[]
    s = deque(s)
    for i in range(len(s)):
        if len(arr) == 0:
            arr.append(s[i])
        else:
            if s[i] == ")" and arr[-1] == "(":
                arr.pop()
            elif s[i] == "]" and arr[-1] == "[":
                arr.pop()
            elif s[i] == "}" and arr[-1] == "{":
                arr.pop()
            else:
                arr.append(s[i])
    if len(arr) == 0:
        return 1
    else:
        return 0

def solution(s):
    # stack 구현
    # 배열 순환 끝나면 회전 구현
    answer = 0
    for i in range(len(s)):
        if bracket(s):
            answer += 1
        s = s[1:] + s[:1]    

            
    return answer    


