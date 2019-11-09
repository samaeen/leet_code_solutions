import collections
class Solution:
    def findRestaurant(self, list1, list2):
    	counter=list(collections.Counter(list1)+collections.Counter(list2))
    	output=''.join(counter[0])
    	print(output)





list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2=["KFC", "Shogun", "Burger King"]
Solution().findRestaurant(list1,list2)