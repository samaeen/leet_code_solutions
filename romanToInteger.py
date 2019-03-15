class Solution:
    def romanToInt(self, s):
        romanNumerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        romanInt = 0
        for i in range(len(s)):
            if i > 0 and romanNumerals[s[i]] > romanNumerals[s[i - 1]]:
                romanInt += romanNumerals[s[i]] - 2 * romanNumerals[s[i - 1]]
            else:
                romanInt += romanNumerals[s[i]]
        return romanInt

print(Solution().romanToInt('MMXI'))
