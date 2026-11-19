# 204. Count Primes

### Difficulty: Medium

## Description
Given an integer n, return the number of prime numbers that are strictly less than n.

 
Example 1:


Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Example 2:


Input: n = 0
Output: 0


Example 3:


Input: n = 1
Output: 0


 
Constraints:


	0 <= n <= 5 * 106

## Submission Details
- **Status**: Accepted
- **Runtime**: 1618
- **Memory**: 65704000
- **Language**: python3

## Code
```python3
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p < n:
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1
        return sum(is_prime)
    


```
