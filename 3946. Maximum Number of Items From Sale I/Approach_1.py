from typing import List
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MAXF = 1500
        cnt = [0] * (MAXF + 1)
        for factor, _ in items:
            for d in range(1, int(factor ** 0.5) + 1):
                if factor % d == 0:
                    cnt[d] += 1
                    if d * d != factor:
                        cnt[factor // d] += 1
        dp = [0] * (budget + 1)
        for factor, price in items:
            gain = cnt[factor]  
            ndp = dp[:]
            for b in range(price, budget + 1):
                ndp[b] = max(ndp[b], dp[b - price] + gain)
            for b in range(price, budget + 1):
                ndp[b] = max(ndp[b], ndp[b - price] + 1)
            dp = ndp
        return max(dp)