class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        def getValidRet(x):
            if x > 2147483647:
                return  2147483647
            elif x < -2147483648:
                return -2147483648
            return x

        ret = ''
        signed = 1
        start = False
        for i in str:
            if i <= '9' and i >= '0':
                if not start:
                    start = True
                ret += i
            elif i == '-' and start:
                return 0
            elif i == '-' and not start:
                start = True
                ret += i
            elif i == '+' and start:
                return 0
            elif i == '+' and not start:
                start = True
            elif i == ' ':
                if start:
                    return getValidRet(int(ret))
            else:
                if not start:
                    return 0
                else:
                    return getValidRet(int(ret))
        else:
            return getValidRet(int(ret))
from datetime import datetime
from time import time
test = Solution()
dt = datetime.now()
now = time()
print(test.myAtoi("+23456789eee777"),\
    datetime.now().microsecond - dt.microsecond)