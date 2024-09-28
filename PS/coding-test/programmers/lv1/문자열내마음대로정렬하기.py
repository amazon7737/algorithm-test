def solution(strings, n):
    # lambda
    return sorted(strings, key=lambda x: (x[n], x))

## 2023.08.08
#두번째 케이스 통과 실패
# 정렬 우선순위 2가지 둬서
# x 순으로 정렬을 해야한다.
print(sorted(strings, key = lambda x: x[n]))
