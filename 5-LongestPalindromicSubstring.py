class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        def getLongestByPoint(point, s, isPointSymmetry):
            longest_str = s[point]
            if isPointSymmetry:
                current_str = s[point]
                left = point - 1
                right = point + 1
            else:
                current_str=""
                left = point
                right = point + 1

            total_length = len(s)
            while True:
                if left < 0 or right > total_length - 1: 
                    if len(current_str) > len(longest_str):
                            longest_str = current_str
                    break
                else:
                    if s[left] == s[right]:
                        current_str = s[left] + current_str + s[right]
                    else:
                        if len(current_str) > len(longest_str):
                            longest_str = current_str
                        break
                left -= 1
                right += 1
            return longest_str
        total_length = len(s)
        longest_str = s[0]
        for i in range(total_length):
            # with this little change, time decrease to 688 ms otherwise is 1029 
            prob_max_length = (total_length - i) * 2 if i + 1 > total_length - i else (i + 1) * 2
            if prob_max_length < len(longest_str):
                continue
            point_str = getLongestByPoint(i, s, True)
            longest_str = point_str if len(point_str) > len(longest_str) else longest_str
            none_point_str = getLongestByPoint(i, s, False)
            longest_str = none_point_str if len(none_point_str) > len(longest_str) else longest_str
        return longest_str

# test = Solution()
# input_str = "abcabba"
# print(input_str, len(input_str))
# output = test.longestPalindrome(input_str)
# print(output, len(output))