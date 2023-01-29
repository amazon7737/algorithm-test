# 잘 풀었다

def solution(cipher, code):
    arr = []
    for i in range(code-1, len(cipher), code):
        arr.append(cipher[i])
    print(arr)
    result = ''
    for i in range(len(arr)):
        result += arr[i]
    return result
