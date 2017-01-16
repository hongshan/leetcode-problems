class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
class State():
    def __init__(self, value):
    # functions to get next state
        # should be a function return a next state
        self.nexts = []
        self.value = value
        self.number = 0
    def setNexts(self, nexts):
        self.nexts = nexts
    def accept(self, input_cha):
        next_state = None
        for f in self.nexts:
            next_state = f(input_cha)
            if next_state:
                break
        else:
            # end of state
            return None
        if next_state:
            return next_state
        else:
            return False
class StateController():
    """docstring for StateController"""
    def __init__(self, pattern):
        self.pattern = pattern
        self.stateToken = []
        self.states = []
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
    def getSingleAcceptedFunction(self, expect_value, next_state, pre_common_state):
        def nextFunction(input):
            print("============")
            if expect_value == '.':
                print("input", input)
                print('current expection', expect_value)
                if next_state:
                    return True, next_state
                else:
                    return True, None
            else:
                print("input", input)
                print('current expection', expect_value)
                if input == expect_value:
                    if next_state:
                        return True, next_state
                    else:
                        return True, None
                else:
                    if pre_common_state:
                        return True, pre_common_state
                    else:
                        return False
        return nextFunction
    def getRepetAcceptedFunction(self, expect_value, next_expect_value, \
        current_state, next_state, pre_common_state):
        def nextFunction(input):
            print("repet input", input, expect_value)
            if expect_value == '.*':
                if next_expect_value and input == next_expect_value[0]:
                    return True, next_state
                else:
                    return True, current_state
            else:
                if next_expect_value and input == next_expect_value[0]:
                    return True, next_state
                elif input == expect_value[0]:
                    return True, current_state
                else:
                    if pre_common_state:
                        return True, pre_common_state
                    return False
        return nextFunction

    def genstates(self):
        self.preProcessPattern()
        for i in range(len(self.stateToken)):

            # self.states.append([])
            # current_state = self.states[len(self.states) - 1]
            next_state = None
            pre_common_state = None
            next_expect_value = None
            if len(self.stateToken[i]) == 1:
                if i + 1 < len(self.stateToken):
                    next_state = i + 1
                for j in range(i, 0):
                    if self.stateToken[j] == ".*":
                        pre_common_state = j
                        break
                self.states.append(self.getSingleAcceptedFunction\
                    (self.stateToken[i], next_state, pre_common_state))
            elif len(self.stateToken[i]) == 2:
                if i + 1 < len(self.stateToken):
                    next_state = i + 1
                    next_expect_value = self.stateToken[i + 1]
                for j in range(i, 0):
                    if self.stateToken[j] == ".*":
                        pre_common_state = j
                        break
                self.states.append(self.getRepetAcceptedFunction\
                    (self.stateToken[i], next_expect_value, \
                        i, next_state, pre_common_state))
    def accept(self, str):
        current_state = 0
        print(current_state)
        for i in str:
            accepted = self.states[current_state](i)
            print("-------", i)
            print(accepted)
            print("********")
            if accepted:
                print("accepted")
                if accepted[0] and accepted[1] != None:
                    current_state = accepted[1]
                elif accepted[0] and accepted[1] == None:
                    return True
            else:
                return False
        if current_state == None:
            return True
        else:
            return False

test = StateController("a*b*b")
teststr = "ab"
test.genstates()
print("accept", test.accept(teststr))


