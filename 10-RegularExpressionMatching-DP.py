class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = self.preProcessPattern(p)
        print(pattern)
        # if pattern:
        #     return self.accept(s, pattern)
        # else:
        #     return False

    def _checkPatternValid(self, rawPattern):
        if len(rawPattern) == 0:
            return False
        if rawPattern[0] == '*':
            return False
        i = 1
        while i < len(rawPattern):
            if rawPattern[i - 1] == '*' and \
                rawPattern[i] == '*':
                return False
            i += 1
        return True
    def preProcessPattern(self, rawPattern):
        #
        temp_token = []
        ret_token = []
        if not self._checkPatternValid(rawPattern):
            return False
        if len(rawPattern) <= 1:
            temp_token.append(rawPattern)
        i = 0
        while i < len(rawPattern):
            if i + 1 < len(rawPattern) and rawPattern[i+1] == '*':
                temp_token.append(rawPattern[i: i+2])
                i += 2
            else:
                temp_token.append(rawPattern[i])
                i += 1
        i = 0
        # make b*b*b to bb*
        temp_token1 = []
        while i < len(temp_token):
            j = i + 1
            if len(temp_token[i]) == 2:
                while j < len(temp_token):
                    if temp_token[i] != temp_token[j]:
                        break
                    j += 1
                else:
                    temp_token1.append(temp_token[i])
                    break
                if temp_token[i][0] == temp_token[j][0]:
                    temp_token1.append(temp_token[j])
                    temp_token[j] = temp_token[i]
                    # temp_token1.append(temp_token[i])
                    i = j
                else:
                    temp_token1.append(temp_token[i])
                    i = j
            else:
                temp_token1.append(temp_token[i])
                i += 1
        # make b*.*c* to .*
        i = 0
        while i < len(temp_token1):
            if len(temp_token1[i]) == 2:
                find_common_symbol = False
                for j in range(i, len(temp_token1)):
                    if len(temp_token1[j]) == 2:
                        if temp_token1[j] == '.*':
                            find_common_symbol = True
                        continue
                    else:
                        if find_common_symbol:
                            ret_token.append('.*')
                            ret_token.append(temp_token1[j])
                        else:
                            ret_token += temp_token1[i:j+1]
                        i = j + 1
                        break
                else:
                    if find_common_symbol == True:
                        ret_token.append('.*')
                    else:
                        ret_token += temp_token1[i:j+1]
                    i = j + 1
            else:
                ret_token.append(temp_token1[i])
                i += 1
        
        return ret_token
    def matchone():
          pass  
    def accept(self, str, pattern):
        print('str, pattern', str, pattern)
        if len(pattern) == 0:
            return True if len(str) == 0 else False

        if len(pattern[0]) == 1:
            if str and str[0] == pattern[0] or pattern[0] == '.' :
                return self.accept(str[1:], pattern[1:])
            else:
                return False
        else:
            if self.accept(str, pattern[1:]):
                return True
            else:
                if str and str[0] == pattern[0][0] or pattern[0][0] == '.':
                    return self.accept(str[1:], pattern)
                else: return False

test = Solution()
teststr = "aa"
print("accept", test.isMatch(teststr, "a"))

