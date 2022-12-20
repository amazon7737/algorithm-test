#1182

import sys
input = sys.stdin.readline
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += s_[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - s_[idx])
    dfs(idx + 1, sum)
n, s = map(int, input().split())
s_ = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)


#2003

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int , sys.stdin.readline().split()))

cnt = 0
for i in range(n):
  tmp = 0
  for h in range(i, n):
    tmp += arr[h]
    if tmp == m:
      cnt += 1
      break
    elif tmp > m:
      break

print(cnt)


