class Solution:
    def addToArrayForm(self, A,K):
    	print([int(i) for i in str(int(''.join(str(i) for i in A))+K)])
  	 	
A = [9,9,9,9,9,9,9,9,9,9]
K = 1
Solution().addToArrayForm(A,K)