# https://leetcode.com/problems/two-sum/

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # approach -> keep a hashmap seen, go through elements (a+b=c, so c-b = a. if present in hashmap -> answer found, else keep adding elements to hashmap.)
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        if remaining in seen:
        # answer found
            return[i, seen[remaining]]
        # else add to hashmap
        seen[value] = i