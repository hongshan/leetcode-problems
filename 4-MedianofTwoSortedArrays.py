#coding:utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        total_len = len(nums1) + len(nums2)
        if total_len % 2:
            return float(self.findKNumber(nums1, nums2, total_len / 2 + 1))
        else:
            return float(self.findKNumber(nums1, nums2, total_len / 2 ) + \
                    self.findKNumber(nums1, nums2, total_len / 2 + 1)) / 2

    def findKNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        def calDet(number):
            return number/2  if (number/2) > 1 else 1
        print("calulate from 0 k:", k)
        current_find = 0
        nums1_start = 0
        nums2_start = 0
        det_find = calDet(k/2)
        current_nums1 = nums1
        current_nums2 = nums2
        whereisK = 0
        def findByDet(nums, det):
            if len(nums) == 0:
                return None, 0
            if len(nums) >= det:
                return nums[det-1], det
            else:
                return current_nums1[len(current_nums1) - 1], len(current_nums1)
        k_value = 0
        while current_find < k:
            current_max1, current_find1 = findByDet(current_nums1, det_find)
            current_max2, current_find2 = findByDet(current_nums2, det_find)
            if not current_max1:
                current_max2, current_find2 = findByDet(current_nums2, k - current_find)
                if current_max2:
                    current_find = k
                    k_value = current_max2
                break
            elif not current_max2:
                current_max1, current_find1 = findByDet(current_nums1, k - current_find)
                if current_max1:
                    current_find = k
                    k_value = current_max1
                break
            elif current_max1 < current_max2:
                current_find += current_find1
                current_nums1 = current_nums1[current_find1:]
                det_find = calDet((k - current_find) / 2)
                k_value = current_max1
            elif current_max1 > current_max2:
                current_find += current_find2
                current_nums2 = current_nums2[current_find2:]
                det_find = calDet((k - current_find) / 2)
                k_value = current_max2
            else:
                current_find += current_find1 + current_find2
                current_nums1 = current_nums1[current_find1:]
                current_nums2 = current_nums2[current_find2:]
                det_find = calDet((k - current_find) / 2)
                k_value = current_max1

        return k_value

        # to be done
            

# test
# 找 nums1 numb2 中 的第m+n/2大的那个数
# 对两个数组进行折半查找，例如nums1[1~x／2]都小于nums2[1~x/2]
# 则说明nums1[1~x/2]都是nums1与nums2合并后小于第x个数字
# 则在接下来的遍历中排出nums1[1~x/2]
# 也就是我们的查找范围缩小了 x/2 
# x = (m+n)/2) / 2
test = Solution()
print(test.findMedianSortedArrays([1,3,4,7,33,100,444,3333,33333], [1,1,1,1,1]))