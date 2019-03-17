class Solution:
    def lengthOfLastWord(self, s):
    	s=s.strip()
    	s=s.split(' ')
    	print(len(s[-1]))
    	

s="a bal"
Solution().lengthOfLastWord(s)