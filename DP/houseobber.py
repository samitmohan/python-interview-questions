# https://leetcode.com/problems/house-robber/description/
# Space -> Instead of keeping entire DP table -> we only keep track of 2 val -> O(1)
# Time -> N houses -> O(N)

class Solution:
    def rob(self, A):
        prev2, prev, cur = 0, 0, 0
        for i in A:
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur
