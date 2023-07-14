#1260 그래프 dfs, bfs 공부 
# https://codesyun.tistory.com/276#DFS%---Depth-First%--Search%-B%--%EA%B-%-A%EC%-D%B-%--%EC%-A%B-%EC%--%A-%--%ED%--%--%EC%--%---
# 1. 일단 트리로 그림을 그리면서 생각하니까 이해가 쉬웠다.
# 2. 트리 따라서 구현을 생각해보니까 깊이우선탐색과 너비우선탐색이 이해가 되었다.
# 3. 재귀함수가 어려웠다. 하지만 구현하기 제일 편하고 효율적인 구조는 재귀함수 활용이라는 것이다.

# dfs 함수 예시
def dfs(graph, v, visited):
	# 현재 노드 방문
    visited[v] = True
    print(v, end=' ')
    
    # 현재 노드와 연결된 다른 노드 방문
    for i in graph[v]:
    	if not visited[i]:
        	dfs(graph, i, visited) # 다시 재방문 시키는 재귀 처리

graph = [
	[],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
# 1 2 7 6 8 3 4 5

#bfs 함수 예시
from collections import deque

def bfs(graph, start, visited):
	queue = deque([start]) # 덱 , 큐 형태로 생각하고 머릿속에 그리기 ( 그림참고)

    # 현재 노드 방문 처리
    visited[start] = True # 방문할때는 True로 바꿈 ( 어차피 재귀처리하면 반복해서 돌아오니까 하는듯)j

    # 큐가 반복될 때까지
    while queue:
    	# 큐에서 원소 꺼내서 출력
        v = queue.popleft() # 큐는 무조건 왼쪽으로 뺀다고 생각하면됨 popleft 기억
        print(v, end=' ')

        # 해당 원소와 연결된, 방문하지 않은 원소 큐에 넣기
        for i in graph[v]:
        	if not visited[v]: # False 이면 그 자리에 추가하고 True 만들어서 방문 처리
            	queue.append(i)
                visited[i] = True 

graph = [
	[],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9 # 전부 False로 초기화

bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6

#1260 문제 해설 #############
from collections import deque
import sys
input = sys.stdin.readline

def dfs(edges, v, visited):
    visited[v] = True
    print(v, end=' ')

    for e in edges[v]:
        if not visited[e]:
            dfs(edges, e, visited)


def bfs(edges, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for e in edges[now]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True


if __name__ == '__main__':
    n, m, v = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    for i in range(1, n + 1):
        edges[i].sort()

    visited = [False] * (n + 1)
    dfs(edges, v, visited)
    print()
    visited = [False] * (n + 1)
    bfs(edges, v, visited)
