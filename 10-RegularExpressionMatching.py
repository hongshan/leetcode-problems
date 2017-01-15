class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        class StateNormal(value):
            def __init__(self, value):
            # functions to get next state
                self.nexts = []
                self.value = value
            def accept(self, input_cha):
                next_state = None
                for f in self.nexts:
                    next_state = f(input_cha)
                    if next_state:
                        break
                if next_state:
                    return True, next_state
                else:
                    return False
class StateController():
    """docstring for StateController"""
    def __init__(self, pattern):
        self.pattern = pattern
        self.stateToken = []
    def checkPatternValid(self):
        if self.pattern[0] == '*':
            return False
        i = 1
        while i < len(self.pattern):
            if self.pattern[i - 1] == '*' and \
                self.pattern[i] == '*':
                return False
            i += 1
        return True
    def preProcessPattern(self):
        #
        if not self.checkPatternValid():
            print("invalid")
            return False
        if len(self.pattern) <= 1:
            self.stateToken.append(self.pattern)
        i = 1
        while i < len(self.pattern):
            if self.pattern[i] == '*':
                self.stateToken.append(self.pattern[i-1: i+1])
                i += 2
            else:
                self.stateToken.append(self.pattern[i - 1])
                i += 1
        print(self.stateToken)
        return True
    def genstates(self):
        pass
        # for t in self.stateToken:
test = StateController("a*b*.*aaaaa......")
test.preProcessPattern()