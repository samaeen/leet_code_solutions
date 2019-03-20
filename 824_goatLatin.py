class Solution:
    def toGoatLatin(self, S):
    	S=S.strip()
    	S=S.split(' ')
    	vowels=['a','A','e','E','i','I','o','O','u','U']
    	goatLang=[]
    	k=0

    	for i in S:
    		if i[0] in vowels:
    			i=i+'ma'
    		if i[0] not in vowels:
    			i=i+i[0]
    			i=i[1:]
    			i=i+'ma'
    		k+=1
    		i=i+'a'*(k)
    		goatLang.append(i)
    	print(' '.join(goatLang))



S="I speak Goat Latin"
Solution().toGoatLatin(S)

a='a'*5
print(a)