class Solution:
    def repeatedNTimes(self, A):
        blankArray=[]
        for i in A:
        	if i not in blankArray:
        		blankArray.append(i)
        	else:
        		print(i)

A=[1,2,3,3]
Solution().repeatedNTimes(A)
            