#10819
import sys
from itertools import permutations

def _10819_1():
  input = sys.stdin.readline
  N = int(input())
  A = list(map(int, input().split()))

  cases = list(permutations(A))

  answer = 0
  for case in cases:
      mid_sum = 0
      for i in range(N - 1):
          mid_sum += abs(case[i] - case[i + 1])
      answer = max(mid_sum, answer)

  print(answer)

import sys

def _10819_2():
  def dfs(depth):
      if depth == N:
          result.append(sum(abs(explore[i] - explore[i + 1]) for i in range(N - 1)))
          return
      for i in range(N):
          if visited[i]:
              continue
          explore.append(A[i])
          visited[i] = 1
          dfs(depth + 1)
          visited[i] = 0
          explore.pop()

  input = sys.stdin.readline
  N = int(input())
  A = list(map(int, input().split()))

  visited = [0] * N
  result, explore = [], []
  dfs(0)
  print(max(result))

#10971
class _10971_2:

  n = int(input())
  maps = []
  for _ in range(n):
      maps.append(list(map(int, input().split())))
  visited = [0] * n
  res = 123456789

  add = 0

class _10971:


  def DFS(f, add, visited):
      global res
      if add > res:
              return
      if sum(visited) == N-1:
          if maps[f][0]:
              res = min(res, add + maps[f][0])
          return
      for i in range(1, N):
          if maps[f][i] and visited[i] == 0:
              visited[i] = 1
              DFS(i, add + maps[f][i], visited)
              visited[i] = 0
  for i in range(1, n):
      if maps[0][i]:
          visited[i] = 1
          DFS(i, maps[0][i], visited)
          visited[i] = 0
  print(res)


#1697

import sys
from collections import deque

class _1697:

  input = sys.stdin.readline

  def bfs():
          q = deque()
          q.append(n)
          while q:
              x = q.popleft()
              if x == k:
                  print(dist[x])
                  break
              for j in (x-1, x+1, x*2):
                  if 0<= j <= MAX and not dist[j]:
                      dist[j] = dist[x] + 1
                      q.append(j)

  MAX = 100000
  n, k = map(int, input().split())
  dist = [0] * (MAX + 1)
  bfs()

#1963

def _1963():
  from collections import deque
  import sys
  input = sys.stdin.readline
  e = [True for i in range(10001)]
  for i in range(2, 101):
    if e[i]:
      j = i * 2
      while j < 10001:
        e[j] = False
        j += i

  def bfs():
    q = deque()
    q.append([a, 0])
    visit = [0 for i in range(10000)]
    visit[a] = 1
    while q:
      num, cnt = q.popleft9)
      if num == b:
        return cnt
      if num < 1000:
        continue
      for i in [ 1, 10, 100, 1000]:
        n = num - num % (i * 10) // i * i
        for j in range(10):
          if visit[n] == 0 and e[n]:
            visit[n] = 1
            q.append([n, cnt + 1])
          n += i

  t = int(input())
  for i in range(t):
    a, b = map(int, input().split())
    result = bfs()
    print(result if result != None else "Impossible")


#9019

def _9019():
  import sys
  from collections import deque

  def oper_D(n):
    res = n * 2
    if res > 9999:
      res %= 10000
    return res

  def oper_S(n):
    res = n
    if res == 0:
      return 9999
    res -= 1
    return res

  def oper_L(n):
    front = n % 1000
    back = n // 1000
    res = front * 10 + back
    return res
  def oper_R(n):
    front = n % 10
    back n // 10
    res = front * 1000 + back
    return res

  def go(s, t):
    queue = deque()
    visited = set()
    queue.append((s, ""))
    visited.add(s)
    while queue:
      cur_num , oper = queue.popleft()
      if cur_num == t:
        print(oper)
        return
      tmp = oper_D(cur_num)
      if tmp not in visited:
        visited.add(tmp)
        queue.append((tmp, oper + "D"))
      tmp = oper_S(cur_num)
      if tmp not in visited:
        visited.add(tmp)
        queue.append((tmp, oper + "S"))
      tmp = oper_L(cur_num)
      if tmp not in visited:
        visited.add(tmp)
        queue.append((tmp, oper + "L"))
      tmp = oper_R(cur_num)
      if tmp not in visited:
        visited.add(tmp)
        queue.append((tmp, oper+"R"))
  for _ in range(int(input())):
    start, target = map(int, input().split())
    #print(start, target)
    go(start, target)

#1525

def _1525():
  from sys import stdin
  input = stdin.readline
  from collections import deque

  dr = (-1, 1, 0, 0)
  dc = (0, 0, -1, 1)

  def bfs():
    check = set([start])
    q = deque([(start, 0)])
    while q:
      temp, cnt = q.popleft()
      if temp == "123456780":
        return cnt
      idx = temp.index("0")
      r, c = idx//3, idx % 3
      for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < 3 and 0 <= nc < 3):
          continue

        nextTemp = list(temp)
        nextIdx = nr * 3 + nc
        nextTemp[idx], nextTemp[nextIdx] = nextTemp[nextIdx], nextTemp[idx]
        nextTemp = ''.join(nextTemp)

        if nextTemp in check:
          continue
        check.add(nextTemp)
        q.append((nextTemp, cnt+1))

    return -1

  start = ""
  for _ in range(3):
    start += ''.join(list(input().split()))

  print(bfs())

#2251
#bfs 문제를 해결 -> 2차원 배열을 사용하여 풀이하는게 쉽다
# 어쩌면 배열, 선형된 데이터 이러한 것들에다가 필요한 알고리즘의 구조를 구현해내면
# 그게 알고리즘의 끝 일 수도 있겠다는 생각을 했다.
def _2251():
  from collections import deque
  import sys
  input = sys.stdin.readline

  a, b, c = map(int, input().strip().split())
  def bfs(a, b, c):
    v = [[False] * (b+1) for _ in range(a+1)]
    q = deque([(0, 0)])
    while q:
      a1, b1 = q.popleft()
      if v[a1][b1]:
        continue
      v[a1][b1] = True
      if a1 > 0:
        if a1 >= b- b1 :
          q.append((a1-b+b1, b))
        else:
          q.append((0, b1+a1))
        if a1 >= a1+b1:
          q.append((b1, b1))
        else:
          q.append((0, b1))
      if b1 > 0:
        if b1 >= a-a1:
          q.append((a, b1-a+a1))
        else:
          q.append((a1+b1, 0))
        if b1 >= a1+b1:
          q.append((a1, b1))
        else:
          q.append((a1, 0))
      if c-a1-b1>0:
        if c-b1>= a:
          q.append((a, b1))
        else:
          q.append((c-b1, b1))
        if c-a1 >= b:
          q.append((a1, b))
        else:
          q.append((a1, c-a1))


    result = set()
    for b1 in range(b+1):
      if v[0][b1]:
        result.add(c-b1)
    return sorted(list(result))
  [print(r, end = ' ') for r in bfs(a, b, c)]

#2186

def _2186():
  import sys
  input = sys.stdin.readline

  n, m, k = map(int, input().split())

  maps = []

  for _ in range(n):
    maps.append(input().rstrip())

  word = input().rstrip()

  visited = [[[-1] * len(word) for _ in range(m)] for _ in range(n)]

  def bfs(y, x, idx):
    global n, m, k, word

    if visited[y][x][idx] != -1:
      return visited[y][x][idx]

    if maps[y][x] != word[idx]:
      return 0

    if idx == len(word) -1:
      return 1
    cnt = 0

    for i in range(-k, k+1):
      if not i:
        continue
      if 0 <= y+i < n:
        cnt += dfs(y+i, x, idx+1)

      if 0 <= x+i < m:
        cnt += dfs(y, x+i, idx+1)
    visited[y][x][idx] = cnt
    return cnt
res = 0
for n in range(n):
  for m in  range(m):
    if maps[n][m] == word[0]:
      res += dfs(n, m, 0)



print(res)

#3108

def _3108():
  from collections import deque

  n = int(input())
  maps = [[0 for _ in range(2001)] for _ in range(2001)]

  startingQue = deque()

  for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    x1 = (x1 + 500) * 2
    y1 = (y1 + 500) * 2
    x2 = (x2 + 500) * 2
    y2 = (y2 + 500) * 2

    for i in range(x1, x2+1):
      maps[y1][i] = 1
      maps[y2][i] = 1
    for i in range(y1, y2+1):
      maps[i][x1] = 1
      maps[i][x2] = 1
    startingQue.append((y1, x1))

startingQue.append((1000, 1000))

dy = [1, -1, 0, 0]
dx = [0, 0,  1, -1]

visited = [[0 for _ in range(2001)] for _ in range(2001)]
res = 0

for q in startingQue:
  if visited[q[0]q[1]]:
    continue

  res += 1
  queue = deque()
  queue.append(q)
  while queue:
    qY, qX = queue.popleft()

    if visited[qY][qX]:
      continue
    visited[qY][qX] = 1

    for i in range(4):
      Y = qY + dy[i]
      X = qX + dx[i]

      if 0 <= Y <= 2000 and 0 <= X <= 2000:
        if maps[Y][X] and not visited[Y][X]:
          queue.append((Y, X))

print(res -1)


