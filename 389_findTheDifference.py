class Solution:
    def findTheDifference(self, s, t):
    	s=list(s)
    	t=list(t)
    	for i in s:
    		t.remove(i)
    	print(t[0])



s = "abcd"
t = "abcde"
Solution().findTheDifference(s,t)

