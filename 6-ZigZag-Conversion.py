class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < 3 or numRows == 1\
            or len(s) < numRows:
            return s

        ret_str = ""
        det1 = numRows*2 - 2
        det2 = numRows*2 - 2
        for i in range(numRows):
            ret_str += s[i]
            index1 = i + det1
            index2 = i + det2 - i * 2
            while index1 < len(s) or \
                    index2 > 0 and index2 < len(s):
                if (i != 0 and i != numRows - 1) \
                    and index2 < len(s):
                   ret_str += s[index2] 
                if index1 < len(s):
                    print(s[index1])
                    ret_str += s[index1]
                index1 += det1
                index2 += det2
        return ret_str

test = Solution()
print(test.convert("ABC", 4))