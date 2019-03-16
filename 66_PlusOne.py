class Solution:
    def plusOne(self, digits):
    	print([int(i) for i in str(int(''.join(str(i) for i in digits))+1)])

#    		
    	 	
digits=[1,2,3]
Solution().plusOne(digits)