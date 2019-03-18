class Solution:
    def hammingDistance(self, x, y):
    	x=int(str(bin(x))[2::],2)
    	y=int(str(bin(x))[2::],2)
    	z=x-y
    	print(z)

x=1
y=4
Solution().hammingDistance(x,y)