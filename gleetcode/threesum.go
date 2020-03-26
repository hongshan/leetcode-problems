package gleetcode

import "fmt"

//nums由数组转化为map O(n)，同时把数组分成正负两部分
//分别处理四种情况
// 0 0 0
// 正 0 负
// 正 正 负
// 负 负 正
func ThreeSum(nums []int) [][]int {
	var positives []int
	var negatives []int
	var zeros []int
	result := [][]int{}
	var numMap = make(map[int]bool)
	var keysMap = make(map[string]bool)
	buildKeys := func(a int, b int, c int) string {
		nums := [3]int{a, b, c}
		for i := 0; i < len(nums); i++ {
			for j := i + 1; j < len(nums); j++ {
				if nums[j] < nums[i] {
					nums[i], nums[j] = nums[j], nums[i]
				}
			}
		}
		return fmt.Sprintln(nums)
	}
	addNums := func(a int, b int, c int) {
		numskey := buildKeys(a, b, c)
		if !keysMap[numskey] {
			result = append(result, []int{a, b, c})
			keysMap[numskey] = true
		}
	}

	for _, v := range nums {
		if v > 0 {
			positives = append(positives, v)
		} else if v < 0 {
			negatives = append(negatives, v)
		} else {
			zeros = append(zeros, v)
		}
		numMap[v] = true
	}
	if len(zeros) > 2 {
		result = append(result, []int{0, 0, 0})
	}
	for i := 0; i < len(positives); i++ {
		if len(zeros) > 0 {
			if numMap[-positives[i]] {
				addNums(-positives[i], 0, positives[i])
			}
		}
		for j := i + 1; j < len(positives); j++ {
			towSum := positives[i] + positives[j]
			if numMap[-towSum] {
				addNums(positives[i], positives[j], -towSum)
			}
		}
	}
	for i := 0; i < len(negatives); i++ {
		for j := i + 1; j < len(negatives); j++ {
			twoSum := negatives[i] + negatives[j]
			if numMap[-twoSum] {
				addNums(negatives[i], negatives[j], -twoSum)
			}
		}
	}
	return result
}
