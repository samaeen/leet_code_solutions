class Solution:
    def reverseWords(self, s):
    	s=s.strip()
    	s=s.split(' ')
    	finalSentence=[]
    	for i in s:
    		a=[j for j in i]
    		b=[j for j in reversed(i)]
    		a=b
    		c=''.join(a)
    		finalSentence.append(c)
    	finalSentence=' '.join(finalSentence)
    	print(finalSentence)

s="Let's take LeetCode contest"
Solution().reverseWords(s)