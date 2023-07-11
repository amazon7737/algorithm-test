
프로그래머스 : 같은숫자는 싫어

def solution(arr):
    ch = []
    ch.append(arr[0])
    for i in range(1, len(arr)):
        if ch[-1] == arr[i]:
            pass
        else:
            ch.append(arr[i])
    return ch        
