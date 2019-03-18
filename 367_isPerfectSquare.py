class Solution:
    def isPerfectSquare(self, num):
    	a=int(str(round(num**(1/2))))
    	b=float(str(num**(1/2)))
    	if a==b:
    		print('ok')
    	else:
    		return False


num=16
Solution().isPerfectSquare(num)
