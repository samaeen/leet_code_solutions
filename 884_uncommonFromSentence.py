class Solution:
    def uncommonFromSentences(self, A, B):
    	A=A.split(' ')
    	B=B.split(' ')
    	blankArray=[]
    	for i in A:
    		if A.count(i)==1 and i not in B:
    			blankArray.append(i)
    	for i in B:
    		if B.count(i)==1 and i not in A:
    			blankArray.append(i)
    	print(blankArray)



A = "apple apple"
B = "sour"
Solution().uncommonFromSentences(A,B)