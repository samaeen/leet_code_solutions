class Solution:
    def fizzBuzz(self, n):
    	fizz=[]
    	for i in range(1,n+1):
    		if i%3==0 and i%5==0:
    			fizz.append('FizzBuzz')
    		elif i%5==0:
    			fizz.append('Buzz')
    		elif i%3==0:
    			fizz.append('Fizz')
    		else:
    			fizz.append(str(i))
    	print(fizz)

n=15
Solution().fizzBuzz(n)
