package gleetcode

func ThreeSumClosest(nums []int, target int) int {
	if len(nums) < 3 {
		return target
	}
	abs := func(a int) int {
		if a >= 0 {
			return a
		} else {
			return -a
		}
	}
	QucikSort(&nums, 0, len(nums)-1)
	closest := nums[0] + nums[1] + nums[2]
	diff := abs(closest - target)
	for k, v := range nums {
		start := k + 1
		end := len(nums) - 1
		first := v
		for start < end {
			sum := first + nums[start] + nums[end]
			if sum > target {
				end--
			} else if sum < target {
				start++
			} else {
				// 找到了相等的
				return sum
			}
			if abs(sum-target) < diff {
				diff = abs(sum - target)
				closest = sum
			}
		}
	}
	return closest
}
