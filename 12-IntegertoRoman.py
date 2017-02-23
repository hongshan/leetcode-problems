class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        分解过程 
        1. 做减法 479 = 500 - 21 21不满足放在左边的条件所以走加法路线 
        2. 做加法 479 = 400 + 79
                       500 - 100 + 50 + 29 
                       CDL + 20 + 9
                       CDL + 10 + 10 + 10 - 1 
                       CDLXXIX
                479 = 470 + 9
                    470 + IX
                    400 + 70 + 9
                    500 - 100 + 50 + 20 + 9
                   （500 - 100） + 50 + 10 + 10 + （10 - 1）
                789 = 780 + 9
                      700 + 80 + 10-1
                      500 + 200 + 80 + 10-1
                      500 + 100+100 + 50+10+10+10 + 10 -1
                      DCCLXXXIX
                

        """
        decimal_set = set(1,  5,   10,  50, 100,  500, 1000)
        roman_set = set( 'I', 'V', 'X', 'L', 'C', 'D', 'M')
        
        # i = 1
        # while num > 0:
        #     tmp = num % 10


# test = Solution()
# print(test.maxArea([1,2,9,7,9,9]))