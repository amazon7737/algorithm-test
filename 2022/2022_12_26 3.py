#1208

n, s = map(int, input().split())

nums = list(map(int, input().split()))

res = 0

leftNums = {}

def DFS(idx, E, add, side):
  global S, N, res
  if idx == E:
    if side == 'L':
      if not add in leftNums:
        leftNums[add] = 1
      else:
        leftNums[add] += 1

    elif S-add in leftNums:
      res += leftNums[S-add]
    return

  DFS(idx+1, E, add+nums[idx], side)
  DFS(idx+1, E, add, side)

DFS(0, N//2, 0, 'L')

DFS(N//2, N, 0, 'R')

if S == 0:
  res -= 1

print(res)

#7453

import sys
from collecitons import defaultdict

input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

first = defaultdict(int)
for i in range(n):
  for j in range(n):
    A_B =A[i] + B[j]
    first[A_B] += 1

answer = 0
for i in range(n):
  for j in range(n):
    A_B = A[i] + B[j]
    first[A_B] += 1


answer = 0
for i in range(n):
  for j in range(n):
    C_D = C[i] + D[j]

    if first.get(-C_D):
      answer += first.get(-C_D)

print(answer)

#2632

import sys

target = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().split())
left = [int(sys.stdin.readline().rstrip()) for _ in range(m)]
right = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

lsum, rsum = [0]*2000001, [0] * 2000001
lsum[0] = rsum[0] = 1
llen,rlen = len(left), len(right)
for i in range(llen):
  s = 0
  for j in range(llen):
    s  += left[(i+j)%m]
    if s > target:
      break

    else:
      lsum[s] += 1

for i in range(rlen):
  s = 0
  for j in range(rlen):
    s += right[(i+j)%n]
    if s > target:
      break
    else:
      rsum[s] += 1
lsum[sum(left)] = rsum[sum(right)] = 1

ans = 0
for i in range(target+1):
  ans += (lsum[i] * rsum[target-i])
print(ans)

#2143

import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

key_set = []
ans = 0

for i in range(n):
  temp = a[i]
  key_set.append(t -temp)
  for j in range(i + 1, n):
    temp += a[j]
    key_set.append(t- temp)

campare = dict().fromkeys(key_set, 0)
for i in key_set:
  compare[i] += 1
for i in range(m):
  temp = b[i]

  try:
    ans += compare[temp]

  except:
    pass

  for j in range(i + 1 , m):
    temp += b[j]
    try:
      ans += compare[temp]
    except:
      pass

print(ans)


