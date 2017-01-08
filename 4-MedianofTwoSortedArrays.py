#coding:utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print(nums1, nums2)
        len1 = len(nums1)
        len2 = len(nums2)

        def getMedian(nums):
        	start = len(nums) / 2
        	print("start:",start)
        	if len(nums) % 2:
        		return (float)(nums[start])
        	else:
        		return (float)(nums[start - 1] + nums[start]) / 2
       	def getMedianIndex(length):
        	if length % 2:
        		return length / 2
        	else:
        		return length / 2 - 1

        # to be done
       		

# test
# 找 nums1 numb2 中 的第m+n/2大的那个数
# 对两个数组进行折半查找，例如nums1[1~x／2]都小于nums2[1~x/2]
# 则说明nums1[1~x/2]都是nums1与nums2合并后小于第x个数字
# 则在接下来的遍历中排出nums1[1~x/2]
# 也就是我们的查找范围缩小了 x/2 
# x = (m+n)/2) / 2
test = Solution()
print(test.findMedianSortedArrays([7,19,20], [1,3,5,6]))