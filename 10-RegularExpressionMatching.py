class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        test = StateController(p)
        return test.accept(s)

class StateController():
    """docstring for StateController"""
    def __init__(self, pattern):
        self.pattern = pattern
        self.stateToken = []
        self.states = []
        self.genstates()
    def checkPatternValid(self):
        if len(self.pattern) == 0:
            return False
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
        temp_token = []
        if not self.checkPatternValid():
            return False
        if len(self.pattern) <= 1:
            temp_token.append(self.pattern)
        i = 0
        while i < len(self.pattern):
            if i + 1 < len(self.pattern) and self.pattern[i+1] == '*':
                temp_token.append(self.pattern[i: i+2])
                i += 2
            else:
                temp_token.append(self.pattern[i])
                i += 1
        i = 0
        # print("tmp token:", temp_token)
        while i < len(temp_token):
            # self.stateToken.append(temp_token[i])
            # print(i)
            j = i + 1
            if len(temp_token[i]) == 2:
                while j < len(temp_token):
                    if temp_token[i] != temp_token[j]:
                        break
                    j += 1
                else:
                    self.stateToken.append(temp_token[i])
                    break
                if temp_token[i][0] == temp_token[j][0]:
                    self.stateToken.append(temp_token[j])
                    temp_token[j] = temp_token[i]
                    # self.stateToken.append(temp_token[i])
                    i = j
                else:
                    self.stateToken.append(temp_token[i])
                    i = j
            else:
                self.stateToken.append(temp_token[i])
                i += 1

        # print("token:", self.stateToken)
        return True
    def getSingleAcceptedFunction(self, expect_value, next_state, pre_common_state):
        def nextFunction(input):
            # print("============")
            if expect_value == '.':
                # print("input", input)
                # print('current expection', expect_value)
                if next_state:
                    return True, next_state
                else:
                    return True, None
            else:
                # print("input", input)
                # print('current expection', expect_value)
                if input == expect_value:
                    if next_state:
                        return True, next_state
                    else:
                        return True, None
                else:
                    if pre_common_state:
                        # print("pre_common_state", pre_common_state)
                        return self.states[pre_common_state](input)
                    else:
                        return False
        return nextFunction
    def getRepetAcceptedFunction(self, expect_value, next_expect_value, \
        current_state, next_next_state, pre_common_state):
        def nextFunction(input):
            # print("repet input", input, expect_value, next_expect_value)
            if expect_value == '.*':
                if next_expect_value and input == next_expect_value[0]:
                    return True, next_next_state + 1
                else:
                    return True, current_state
            else:
                if next_expect_value and input == next_expect_value[0]:
                    return True, next_next_state
                elif input == expect_value[0]:
                    return True, current_state
                else:
                    if pre_common_state:
                        # print("pre common .*", pre_common_state)
                        return self.states[pre_common_state](input)
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
            next_next_state = None
            if len(self.stateToken[i]) == 1:
                if i + 1 < len(self.stateToken):
                    next_state = i + 1
                for j in range(0, i):
                    if self.stateToken[j] == ".*":
                        pre_common_state = j
                        break
                self.states.append(self.getSingleAcceptedFunction\
                    (self.stateToken[i], next_state, pre_common_state))
            elif len(self.stateToken[i]) == 2:
                if i + 1 < len(self.stateToken):
                    next_state = i + 1
                    next_expect_value = self.stateToken[i + 1]
                for j in range(0, i):
                    if self.stateToken[j] == ".*":
                        pre_common_state = j
                        break
                self.states.append(self.getRepetAcceptedFunction\
                    (self.stateToken[i], next_expect_value, \
                        i, next_state, pre_common_state))
    def accept(self, str):
        current_state = 0
        # print(current_state)
        if len(self.states) == 0:
            return False
        for index in range(len(str)):
            i = str[index]
            accepted = self.states[current_state](i)
            print("-------", i)
            print(accepted)
            print("********")
            if accepted:
                print("next state", accepted[1])
                if accepted[0] and accepted[1] != None:
                    current_state = accepted[1]
                elif accepted[0] and accepted[1] == None:
                    if index == len(str) - 1:
                        return True
                    else:
                        return False
            else:
                return False
        # input is too short, to check if the rest state can be end state
        if current_state == len(self.states) - 1:
            return True
        else:
            for i in range(current_state,len(self.states)):
                if len(self.stateToken[i]) == 2:
                    continue
                else:
                    return False

            return True

test = Solution()
teststr = "a"
print("accept", test.isMatch(teststr, "aa"))


