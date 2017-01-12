class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = 0
        signed = 1
        if x < 0:
            x = -x
            signed = -1
        while x:
            a = x % 10
            out = out * 10 +  a
            x = (x - a) / 10
        return out * signed

test = Solution()
print(test.reverse(1534236469))