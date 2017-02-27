class Solution(object):
    def findRoman(self, num):
        num_map = {
          1: 'I',
          2: 'II',
          3: 'III',
          4: 'IV',
          5: 'V',
          6: 'VI',
          7: 'VII',
          8: 'VIII',
          9: 'IX',
          10: 'X',
          20: 'XX',
          30: 'XXX',
          40: 'XL',
          50: 'L',
          60: 'LX',
          70: 'LXX',
          80: 'LXXX',
          90: 'XC',
          100: 'C',
          200: 'CC',
          300: 'CCC',
          400: 'CD',
          500: 'D',
          600: 'DC',
          700: 'DCC',
          800: 'DCCC',
          900: 'CM',
          1000: 'M',
          2000: 'MM',
          3000: 'MMM',
        }
        ret = num_map.get(num)
        if ret :
          return True, ret
        else:
          return False
    def divide(self, num):
      base = 10
      while num % base == 0:
        base *= 10
      else:
        return num - num % base, num % base


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str 
        """
        ret = ''
        left, right = self.divide(num)
        if right:
          finded = self.findRoman(right)
          if finded:
            ret = finded[1] + ret
        if left:
          finded = self.findRoman(left)
          if finded:
            ret = finded[1] + ret
          else:
            ret = self.intToRoman(left) + ret
        return ret
# test = Solution()
# print(test.intToRoman(2034))