class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_water = 0
        while i < j :
            temp = (j - i) * (height[i] \
                if height[i] < height[j] else height[j])
            if temp > max_water :
                max_water = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
# test = Solution()
# print(test.maxArea([1,2,9,7,9,9]))