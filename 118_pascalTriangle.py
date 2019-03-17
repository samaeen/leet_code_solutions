class Solution:
    def generate(self, numRows):
    	for i in range(numRows):
    		if i>0:
    			print('x'*i)
    		else:
    			print('1')


numRows=5
Solution().generate(numRows)