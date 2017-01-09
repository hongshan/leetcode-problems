class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
        	return 0

        max_length = 1
        current_substr = s[0]
        for i in range(1, len(s)):
        	find_pos = current_substr.find(s[i])
        	if find_pos == -1:
        		current_substr += s[i]
        	else:
        		if len(current_substr) > max_length:
        			max_length = len(current_substr)
        		current_substr = current_substr[find_pos+1:] + s[i]
        else:	
	       	if (len(current_substr) > max_length):
	        			max_length = len(current_substr)
        return max_length
        	

# test code
# test = Solution()
# print(test.lengthOfLongestSubstring("abcaf"))
