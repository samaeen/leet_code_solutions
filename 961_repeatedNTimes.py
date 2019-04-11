class Solution:
    def repeatedNTimes(self, A):
        blankArray=[]
        for i in A:
        	if i not in blankArray:
        		blankArray.append(i)
        	else:
        		return i
        

S="xxxyyz"
Solution().largeGroupPositions(S)