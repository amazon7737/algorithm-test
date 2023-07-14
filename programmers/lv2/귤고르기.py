def solution(k, tangerine):
    answer = 0
    a = {}

    for i in tangerine:
        if i in a:
            a[i] += 2
        else:
            a[i] = 1

    # 제일 많이 체크된 순서대로 정렬이 됨. )
    print(dict(sorted(a.items(), key = lambda x: x[1], reverse = True)))
    a = dict(sorted(a.items(), key = lambda x: x[1], reverse = True))

    for i in a:
        if k <= 0:
            return answer
        k -= a[i]
        answer += 1
        print("i:", i)

    return answer
  
  solution(6, [1,3,2,5,4,5,2,3])
