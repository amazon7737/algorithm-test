from collections import deque

# deque 사용
# 규칙성 찾기 -> 결국 수가 제일 큰 애들부터 판단해야 누적된 값이 최솟값이 될수 있다.
# 작은 수부터 더해야한다는 생각의 방향을 바꿔보니 해결되었다.
def solution(A,B):
    A = deque(sorted(A))
    B=deque(sorted(B))
    a=0
    for i in range(len(A)):
        a += A[-1]*B[0]
        A.pop();B.popleft()
    return a
