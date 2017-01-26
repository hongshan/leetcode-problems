class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        test = StateController(p)
        # return test.accept(s)

class StateController():
    """docstring for StateController"""
    def __init__(self, pattern):
        self.pattern = pattern
        self.stateToken = []
        self.states = {}
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
        print('first step', temp_token)
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
        print('second step', temp_token1)
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
                            self.stateToken.append('.*')
                            self.stateToken.append(temp_token1[j])
                        else:
                            self.stateToken += temp_token1[i:j+1]
                        i = j+1
                        break
                else:
                    if find_common_symbol != None:
                        self.stateToken.append('.*')
                    else:
                        self.stateToken.append(temp_token1[i:j])
                    i = j
            else:
                self.stateToken.append(temp_token1[i])
                i += 1
        print(self.stateToken)

        return True
    def pprpcess(self, pattern, input_ch):
        accept = False
        if pattern[0] == input_ch || pattern[0] == '.':
            accept = True
        return accept
    def genstates(self):
        self.preProcessPattern()
        for i in range(0, len(self.stateToken)):
            current_state = {}
            p = self.stateToken[i]
            current_state[p[0]] = []
            if len(p) == 1:
                for j in range(j,len(self.stateToken)):
                    accept = self.pprpcess(self.stateToken[j], p[0])
                    if len(self.stateToken[j]) == 1:
                        current_state[p].append(j)
                        break
                    else:
                        if accept:
                            current_state[p].append(j)
            else:
                for j in range(i,len(self.stateToken)):
                    accept = self.pprpcess(self.stateToken[j], p[0])
                    if accept:
                        current_state[p].append(j)
                    if len(self.stateToken[j]) == 1:
                        break


        print(self.states)
        return self.states
        

    def accept(self, str):
        current_state_number = 0
        
        if len(self.states) == 0:
            return False
        for index in range(len(str)):
            print("current state", current_state_number)
            input_ch = str[index]
            print("input char", input_ch)
            if current_state_number < len(self.states):
                state = self.states[current_state_number]
                print(state)
                if state.get(input_ch):
                    current_state_number = state.get(input_ch)
                elif state.get('others'):
                    current_state_number = state.get('others')
                else:
                    return False
            else:
                return False
        else:
            if current_state_number == len(self.states):
                return True
            else:
                for i in range(current_state_number,len(self.states)):
                    if len(self.stateToken[i])  ==  1:
                        return False
                return True

test = Solution()
teststr = "a"
print("accept", test.isMatch(teststr, "a*b*a"))


