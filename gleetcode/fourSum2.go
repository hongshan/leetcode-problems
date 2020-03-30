package gleetcode

import (
	"fmt"
	"sort"
)

func FourSum1(nums []int, target int) [][]int {
	ret := [][]int{}
	keysmap := map[string]bool{}
	sort.Ints(nums)

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
	f := func(a int, d int) {
		b := a + 1
		c := d - 1
		for b < c {
			if nums[a]+nums[b]+nums[c]+nums[d] < target {
				b++
			} else if nums[a]+nums[b]+nums[c]+nums[d] > target {
				c--
			} else {
				newline := []int{nums[a], nums[b], nums[c], nums[d]}
				if !haskeys(&newline) {
					ret = append(ret, newline)
				}
				b++
				c--
			}
		}
	}
	a := 0
	d := len(nums) - 1
	for a < len(nums)-3 {
		d = len(nums) - 1
		for a < d {
			f(a, d)
			d--
		}
		a++
	}
	return ret
}
