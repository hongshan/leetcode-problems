package gleetcode

import (
	"fmt"
	"sort"
)

func FourSum(nums []int, target int) [][]int {
	nummap := map[int][][2]int{}
	allsums := []int{}
	ret := [][]int{}
	keysmap := map[string]bool{}
	haskeys := func(line *[]int) bool {
		sort.Ints(*line)
		key := fmt.Sprintln(line)
		if _, ok := keysmap[key]; ok {
			return true
		} else {
			keysmap[key] = true
		}
		return false
	}
	diffnum := func(a *[][2]int, b *[][2]int) *[][]int {
		ret := [][]int{}
		diffpoint := func(p1 *[2]int, p2 *[2]int) bool {
			for _, v1 := range p1 {
				for _, v2 := range p2 {
					if v1 == v2 {
						return false
					}
				}
			}
			return true
		}
		for _, v1 := range *a {
			for _, v2 := range *b {
				if diffpoint(&v1, &v2) {
					newline := []int{nums[v1[0]], nums[v1[1]], nums[v2[0]], nums[v2[1]]}
					if !haskeys(&newline) {
						// fmt.Println(newline)
						ret = append(ret, newline)
					}
				}
			}
		}
		return &ret
	}

	// a , b   属于nums，且不相等，记录下所有a b的和与坐标
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			sum := nums[i] + nums[j]
			if _, ok := nummap[sum]; ok {
				nummap[sum] = append(nummap[sum], [2]int{i, j})
			} else {
				allsums = append(allsums, sum)
				nummap[sum] = [][2]int{[2]int{i, j}}
			}

		}
	}

	sort.Ints(allsums)
	start := 0
	end := len(allsums) - 1
	for start <= end {
		sum1 := allsums[start]
		sum2 := allsums[end]
		if sum1+sum2 < target {
			start++
		} else if sum1+sum2 > target {
			end--
		} else {
			point1 := nummap[sum1]
			point2 := nummap[sum2]
			ret = append(ret, *diffnum(&point1, &point2)...)
			start++
			end--
		}
	}
	return ret
}
