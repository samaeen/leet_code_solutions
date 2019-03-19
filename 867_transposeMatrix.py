class Solution:
    def transpose(self, A):
    	print([[A[j][i] for j in range(len(A))] for i in range(len(A))])


A=[[1,2,3],[4,5,6],[7,8,9]]
Solution().transpose(A)