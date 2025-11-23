MOD = 10**9 + 7

def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    
    pre_sum = [0] * (n + 1)
    pre_sum[1] = 1
    
    for i in range(2, n + 1):
        left = max(1, i - forget + 1)
        right = i - delay
        if right >= left:
            dp[i] = (pre_sum[right] - pre_sum[left - 1]) % MOD
        pre_sum[i] = (pre_sum[i - 1] + dp[i]) % MOD
    
    start = max(1, n - forget + 1)
    return (pre_sum[n] - pre_sum[start - 1]) % MOD