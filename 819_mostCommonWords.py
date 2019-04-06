##eta keno kaj korlo na???
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned=set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        print(words)
        for i in words:
            if i in banned:
                words.remove(i)
        dic = collections.Counter(words).most_common(1)
        return dic[0][0]

##eta kaj korse

import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned=set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]
                