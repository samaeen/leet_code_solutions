##nope this is the easiest
class Solution:
    def sortedSquares(self, A):
    	a=sorted([i**2 for i in A])
    	print(a)

A=[-4,-1,0,3,10]
Solution().sortedSquares(A)