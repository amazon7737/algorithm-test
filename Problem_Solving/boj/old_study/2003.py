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
