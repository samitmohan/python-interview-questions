# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # merge intervals problem
    intervals.sort(key = lambda x: x[1])
    count = 0
    currEnd = intervals[0][1]
    for start, end in intervals[1:]:
      if start >= currEnd:
        currEnd = end
      else:
        count += 1
    return count
