class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 2147483647 or x < 0:
            return  False
        out = 0
        base = x
        while x:
            out = out * 10 +  x % 10
            # more slow.......
            if out == base:
                return True
            x = x / 10
        return out == base
test = Solution()
print(test.isPalindrome(1221))