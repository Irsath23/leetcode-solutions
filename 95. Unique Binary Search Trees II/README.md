# 95. Unique Binary Search Trees II

### Difficulty: Medium

## Description
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 
Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]


Example 2:


Input: n = 1
Output: [[1]]


 
Constraints:


	1 <= n <= 8

## Submission Details
- **Status**: Accepted
- **Runtime**: 4
- **Memory**: 20480000
- **Language**: python3

## Code
```python3
class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        def build(start, end):
            if start > end:
                return [None]
            result = []
            for root_val in range(start, end + 1):
                left_trees = build(start, root_val - 1)
                right_trees = build(root_val + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        result.append(root)
            return result
        return build(1, n)
```
