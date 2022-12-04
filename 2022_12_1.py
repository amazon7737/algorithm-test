
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

#5014

def _5014():
  from collections import deque

  F, S, G, U, D = map(int, input().split())

  queue = deque()
  queue.append((S, 0))

  visited = [0] * (F+1)
  visited[S] = 1
  res = F

  while queue:
    s, cnt = queue.popleft()

    if s == G:
      res = min(res, cnt)
      break
    if s + U <= F and not visited[s+U]:
      visited[s+U] = 1
      queue.append((s+U, cnt+1))

    if s - D >= 1 and not visited[s-D]:
      visited[s-D] = 1
      queue.append((s-D, cnt+1))


if res == F:
  print("use the stairs")

else:
  print(res)

#1759

#조합
def _1759():
  import sys
  from itertools import combinations

  input = sys.stdin.readline
  L, C = map(int, input().split())
  alphabet = lsit(input().split())
  alphabet.sort()

  def check(string):
    count = 0
    for alpha in string:
      if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
        count += 1

    return count
  
  for case in combinations(alphabet, L):
    if check(case) >= 1 and (len(case) - check(case)) >= 2:
      print(''.join(case))

#백트래킹

def _1759_2():
  import sys

  input = sys.stdin.readline

  L, C = map(int, input().split())
  alphabet = list(input().split())
  alphabet.sort()
  visited = [0] * C

  def check(string):
    count = 0
    for alpha in string:
      if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
        count += 1
      return count

  def dfs(depth, string, idx):
    if depth == L:
      if check(string) >= 1 and (len(string) - check(string)) >= 2:
        print(''.join(string))
      return

    for i in range(C):
      if idx < i:
        if not visited[i]:
          visited[i] = 1
          string.append(alphabet[i])
          dfs(depth + 1, string , i)
          visited[i] = 0
          string.pop()


  dfs(0, [], -1)


#2580

def _2580():
  import sys

  board = [list(map(int, input().split())) for _ in range(9)]

  emptySpace = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

  def candidating(y, x):
    numbers = [i+1 for i in range(9)]

    for k in range(9):
      if board[y][k] in numbers:
        numbers.remove(board[y][k])
      if board[k][x] in numbers:
        numbers.remove(board[k][x])
    y = y//3
    x = x//3

    for i in range(y*3, (y+1)*3):
      for j in range(x*3, (x+1)*3):
        if board[i][j] in numbers:
          numbers.remove(board[i][j])

    return numbers

  def dfs(count):
    if count == len(emptySpace):
      for row in board:
        print(*row)
      return
    (i, j) = emptySpace[count]
    candi = candidating(i, j)

    for num in candi:
      board[i][j] = num
      dfs(count + 1)
      board[i][j] = 0


  dfs(0)

#1987

def _1987():
  import sys

  input = sys.stdin.readline
  dy = [1, -1, 0, 0]
  dx = [0, 0, 1, -1]

  def bt(y, x, cnt):
    global ans

    visited[ord(board[y][x]) - ord('A')] = True

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if 0 <= ny < r and 0 <= nx < c:
        index = ord(board[ny][nx]) - ord('A')
        if visited[index] == False:
          bt(ny, nx, cnt + 1)
          visited[index] = False

    ans = max(ans,cnt)

  r, c = map(int, input().split()
  board = [list(input()) for _ in range(r)]
  visited = [0] * 26
  ans = 0

  bt(0, 0, 1)
  print(ans)

#6603


#itertool -> combination 사용
def _6603():
  import sys
  from itertools import combinations

  input = sys.stdin.readline

  while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
      break

    length = nums.pop(0)

    for comb in combinations(nums, 6):
      temp = list(map(str, comb))
      print(" ".join(temp))

    print()

#DFS / 백트래킹

def _6603_2():

  import sys
  input = sys.stdin.readline

  def dfs(lotto, nums, visited):
    if len(lotto) == 6:
      for i in range(6):
        print(nums[lotto[i]], end = ' ')
      print()
      return

    t_visited = visited[:]
    for i in range(len(t_visited)):
      if not t_visited[i]:
        t_visited[i] = True
        dfs(lotto + [i], nums, t_visited)

    while True:
      nums = list(map(int, input().split()))
      if len(nums) == 1 and nums[0] == 0:
        break
      length = nums.pop(0)

      visited = [False] * len(nums)
      dfs([], nums, visited)
      print()
