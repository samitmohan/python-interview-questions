# https://leetcode.com/problems/delete-columns-to-make-sorted/
class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
      # go col by col and then row by row -> if any char less than prev char -> not sorted -> count++
      # or a little zip magic
      # [abc]
      # [cdf]
      # [ghi]
      # check if a, c, g | | b, d, h | | c, f, i in sorted order
    count = 0
    for char in zip(*strs):
      if list(char) != sorted(char):
        count += 1
    return count
