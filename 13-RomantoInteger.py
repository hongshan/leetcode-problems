class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map = {
          'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000,
        }
        ret = 0
        i = 0
        while i < len(s):
            left = num_map.get(s[i])
            if i + 1 < len(s):
                right = num_map.get(s[i + 1])
                if left < right:
                    ret = ret -left + right
                    i += 2
                else:
                    ret += left
                    i += 1
            else:
                ret += left
                i += 1
        return ret
# test = Solution()
# print(test.romanToInt('MCMXCVI'))
# 1996
