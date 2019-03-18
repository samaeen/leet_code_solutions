class Solution:
    def addDigits(self, num):
    	a=str(num)
    	while True:
    		s=0
    		for num in a:
    			s+=int(num)
    		if s<10:
    			print(s)
    		a=str(s)

num=38
#Solution().addDigits(num)
a=20
while 