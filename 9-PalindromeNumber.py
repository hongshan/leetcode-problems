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
            a = x % 10
            out = out * 10 +  a
            x = (x - a) / 10
        print(121)
        if out == base:
            return True
        return False
test = Solution()
print(test.isPalindrome(1333331))