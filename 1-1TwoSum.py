class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums_dict.get(nums[i]):
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = []
                nums_dict[nums[i]].append(i)
        for i in range(len(nums)):
            right = nums_dict.get(target - nums[i])
            if right != None:
                if nums[i] == target - nums[i]:
                    if len(right) >= 2:
                        return right[0], right[1]
                else:
                    return i, right[0]

test = Solution()
print(test.twoSum([3,2,4], 6))