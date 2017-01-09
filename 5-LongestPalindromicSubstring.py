class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        longest_str = ""
        current_str = ""
        total_length = len(s)
        print(total_length)
        longest_str = s[0]
        for i in range(total_length):
            print("start", i)
            prob_max_length = total_length - i if i + 1 > total_length - i else i + 1
            current_str = s[i]
            p1_left = i - 1
            p1_right = i + 1
            if prob_max_length < max_length:
                print("nothing")
                continue
            while True:
                print(p1_left, p1_right)
                if p1_left < 0 or p1_right > total_length - 1: 
                    print("no hope", p1_left, p1_right)
                    if len(current_str) > len(longest_str):
                            longest_str = current_str
                    break
                else:
                    if s[p1_left] == s[p1_right]:
                        print("find same")
                        current_str = s[p1_left] + current_str + s[p1_right]
                    else:
                        if len(current_str) > len(longest_str):
                            longest_str = current_str
                            print("find long", longest_str)
                        break
                p1_left -= 1
                p1_right += 1
            print("next")
        return longest_str

test = Solution()
print(test.longestPalindrome("abcbghghabcddcbaff"))