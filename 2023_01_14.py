#완주하지못한선수 복습 ( 프로그래머스)

def solution(participant, completion):
  answer = ""
  participant.sort()
  completion.sort()
  for i in range(len(participant)-1):
    if participant[i] != completion[i]:
      answer = participant[i]
      break
  if answer = "":
    answer = participant[-1]
  return answer


# 같은 숫자은 싫어 복습(프로그래머스)

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer


# 올바른 괄호 복습(프로그래머스)  

def solution(s):
    answer = True
    arr = []
    a = ""
    for i in range(len(s)):
        a = s[i]
        if a == "(":
            arr.append("(")
        elif a == ")":
            try:
                arr.pop()
            except:
                return False
    if arr != []:
        return False
    return True


# k번째 수 복습 ( 프로그래머스)

def solution(array, commands):
    arr = []
    arr2 = []
    for x in range(len(commands)):
        i = commands[x][0]
        j = commands[x][1]
        k = commands[x][2]
        arr = array[i-1:j]
        arr.sort()
        s = arr[k-1]
        arr2.append(s)
    return arr2

# boj 1260 복습(그래프)

from collections import deque

n, m , v = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()
visited = [False] * (n+1)


def dfs(graph, v):
    print(v, end = ' ')
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w)

def bfs(graph, start):
    visited = [False] * (n+1)
    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
dfs(graph,v)
print()
bfs(graph,v)

