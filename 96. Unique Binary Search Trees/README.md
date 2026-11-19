# 96. Unique Binary Search Trees

### Difficulty: Medium

## Description
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 
Example 1:


Input: n = 3
Output: 5


Example 2:


Input: n = 1
Output: 1


 
Constraints:


	1 <= n <= 19

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19172000
- **Language**: python3

## Code
```python3
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        return dp[n]


        
```
