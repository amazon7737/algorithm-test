def solution(age):
    arr = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    age = str(age)
    answer = ''
    b = len(age)
    for i in range(0, b):
    #	answer += arr[age[i]]
        a = age[i]    
        a = int(a)
        answer += arr[a]
    return answer
