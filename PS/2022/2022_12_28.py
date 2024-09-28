#1182

import sys
input = sys.stdin.readline

total_cnt = 0

def dfs(index, n, s, cnt):
    global total_cnt
    if index == n: 
        return
    if cnt + nums[index] == s:
        total_cnt += 1
    dfs(index+1, n, s, cnt) # 0 
    dfs(index+1, n, s, cnt + nums[index]) # num

n, s = map(int, input().rsplit())
nums = sorted(list(map(int, input().rsplit())))

dfs(0, n, s, 0)

print(total_cnt)


