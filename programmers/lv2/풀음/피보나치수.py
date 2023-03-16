def solution(n):
    dp = [0, 1]
    for i in range(n+1):
        dp.append(dp[i]+dp[i+1])
    return dp[n]%1234567
