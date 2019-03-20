class Solution:
    def reverseVowels(self, s):
        vowels=['a','A','e','E','i','I','o','O','u','U']
        reversedVowel=[]
        balArray=[]
        for i in s:
            if i in vowels:
                reversedVowel.append(i)
        for i in s:
        	if i in vowels:
        		i=reversedVowel[::-1]
        		balArray.append(i)
        	else:
        		balArray.append(i)
       	print(balArray)

s="leetcode"
Solution().reverseVowels(s)



