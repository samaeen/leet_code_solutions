class Solution:
    def validSquare(self, p1, p2, p3, p4):
    	a=abs(p1[0]-p2[0])
    	b=abs(p1[1]-p2[1])
    	c=abs(p3[0]-p4[0])
    	d=abs(p3[1]-p4[1])
    	if a==b==c==d:
    		print('ok')
    	print(a)
    	print(b)
    	print(c)
    	print(d)

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
Solution().validSquare(p1,p2,p3,p4)