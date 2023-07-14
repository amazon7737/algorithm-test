def solution(s):
    # !
# answer => 인덱스 # arr => 들어간 문자추가
# arr => 딕셔너리를 사용하면 문자를 부르면 그 문자의 인덱스가 들어가고
# 인덱스를 부르면 그 인덱스에 해당하는 문자가 들어감
    answer = []; arr = {};
    
    for idx, word in enumerate(list(s)):
        if word not in arr:
            answer.append(-1)
            arr[word] = idx
        else:
            answer.append(idx - arr[word])
            arr[word] = idx
    return answer
