# 🎯 Subset Sum Equals to Target

## 💡 Problem Statement

Given an array `arr` of `n` integers and an integer `target`, determine if there is a **subset** of the given array with a sum equal to the given target.

---

## 🧠 Hint

Use **Dynamic Programming (DP)** to solve this problem efficiently. Create a 2D DP table where `dp[i][j]` represents whether it’s possible to achieve a sum of `j` using the first `i` elements.

---

## 🔍 Examples

### ✅ Example 1:
- **Input:** `arr = [1, 2, 7, 3]`, `target = 6`  
- **Output:** `True`  
- **Explanation:** Subset `(1, 2, 3)` sums to `6`.

### ❌ Example 2:
- **Input:** `arr = [2, 3, 5]`, `target = 6`  
- **Output:** `False`  
- **Explanation:** No subset sums to `6`.

### ✅ Example 3:
- **Input:** `arr = [7, 54, 4, 12, 15, 5]`, `target = 9`  
- **Output:** `True`

---

## 🧑‍💻 Solution (Python)

```python
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = True  # Target 0 is always possible

        if arr[0] <= target:
            dp[0][arr[0]] = True

        for ind in range(1, n):
            for j in range(1, target + 1):
                nottake = dp[ind - 1][j]
                take = False
                if arr[ind] <= j:
                    take = dp[ind - 1][j - arr[ind]]
                dp[ind][j] = take or nottake

        return dp[n - 1][target]
