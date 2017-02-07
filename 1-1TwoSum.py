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
        print(nums_dict)
        for i in range(0,target/2 + 1):
            left = nums_dict.get(i)
            right = nums_dict.get(target-i)
            if left != None and right != None:
                if i == target-i:
                    return  left[0], left[1]
                else:
                    return left[0], right[0]
test = Solution()
print(test.twoSum([3,3,4], 6))