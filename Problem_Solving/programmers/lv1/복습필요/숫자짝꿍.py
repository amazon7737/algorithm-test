def solution(X, Y):
    # x y 의 짝꿍이 존재하지 않으면 -1 
    # x y 의 공통으로 나타나는 정수 k 로 만들수 있는 가장 큰 정수 -> 두수의 짝꿍
    
    # 짝꿍이 0 만 있다 -> 짝꿍은 0
    
   	# arr -> 공통되어 등장 -> 추가

    # topick -> 가서 나올수 있는 모든 경우 -> 에서 수들의 모음 -> arr2 -> 최댓값 찾기
    # 테스트 5개 시간초과 코드..
    arr=list(map(str, X));arr2=list(map(str, Y));arr3=[]
    arr.sort(reverse = True);arr2.sort(reverse = True)
    print("arr:",arr)
    print("arr2:",arr2)
    for i in range(len(arr), -1, -1):
        for j in range(len(arr2), -1, -1):
            try:
                if arr[i] == arr2[j]:
                    arr3.append(arr[i])
                    arr.pop()
                    arr2.pop()
                else:
                    #arr.pop()
                    arr2.pop()
            except IndexError:
                pass
        print("arr3:",arr3)
        
    if arr3 == []:
        return str(-1)
    
    a = ''; cnt = 0
    arr3.sort(reverse = True)
    
    for i in range(len(arr3)):
        a += arr3[i]
    if int(a) == 0:
        return str(0)
    return a
           

# count 를 이용한 풀이..

def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    #print(answer)

    if answer == '':
        return str(-1)

    # 효율성.. !
    elif len(answer) == answer.count('0'):
        return '0'

    # if int(answer) == 0: -> return str(0) 이거는 효율성 폭발햇음..

    return answer
