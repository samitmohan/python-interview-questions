# https://leetcode.com/problems/daily-temperatures/solutions/1574808/c-python-3-simple-solutions-w-explanation-examples-images-2-monotonic-stack-approaches/

# https://leetcode.com/problems/daily-temperatures/
'''
 Monotonic Decr Stack -> put elements in stack
 73 next number -> 74 -> 74 - 73 > 0 so next number is warmer temperature.
 pop 73 and print 1 (i - stackInd) and put 74 in it.
 next number -> 75 (69-75) (71-75) (72-75) all negative -> push in stack and find i - stackInd
 76-75 > 0 -> pop all and find i - stackInd
 Calculating difference using the index.
'''
class Solution(object):
  def dailyTemperatures(self, T):
    ans = [0] * len(T) # empty array
    stack = [] # pair : [temp, index]
    for i, t in enumerate(T):
      while stack and T[stack[-1]] < t: # curr elem greater
        curr = stack.pop()
        ans[curr] = i - curr # index
      stack.append(i) # elem add
    return ans
