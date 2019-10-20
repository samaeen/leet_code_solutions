class Solution:
    def removeOuterParentheses(self, S):
    	count=0
    	outString=[]
    	first=0
    	for i in range(len(S)):
    		if S[i]=='(':
    			count+=1
    		if S[i]==')':
    			count-=1
    		if count==0:
    			outString.append(S[first+1:i])
    			first=i+1
    	return ''.join(outString)
    			


Solution().removeOuterParentheses('(()())(())')