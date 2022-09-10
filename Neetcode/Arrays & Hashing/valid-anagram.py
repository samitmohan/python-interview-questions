# https://leetcode.com/problems/valid-anagram/

# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # approach -> sorting both will result in the same thing (tan / nat => ant)
        for x in "abcdefghijklmnopqrstuvwxyz":
            if sorted(s) == sorted(t):
                return True
        return False


# ​Time Complexity -> O(nlogn)