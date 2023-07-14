def solution(n):
    dp = [0, 1]
    for i in range(n+1):
        dp.append(dp[i]+dp[i+1])
    return dp[n]%1234567


# -------

# 다시 한번더 풀어보았는데 깔끔.

def solution(n):
    dp = []
    dp.append(0);dp.append(1)

    for i in range(1, n+2):
        dp.append(dp[i-1]+ dp[i])
        #print("dp:",dp)
    return dp[n]%1234567
