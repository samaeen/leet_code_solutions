class Solution:
    def arrangeCoins(self, n):
    	coins=1
    	while n>=0:
    		n-=coins
    		coins+=1
    		print(coins)

    	return coins-2



n=5
Solution().arrangeCoins(n)