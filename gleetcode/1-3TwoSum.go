package gleetcode

func TwoSum2(nums []int, target int) []int {
	type element []int
	hash_map := make(map[int]element)
	for i := 0; i < len(nums); i++ {
		item, ok := hash_map[nums[i]]
		if ok {
			item = append(item, i)
		} else {
			hash_map[nums[i]] = element{i}
		}
	}
	for i := 0; i < len(nums); i++ {
		right_num := target - nums[i]
		if item, ok := hash_map[right_num]; ok {
			for _, index_right := range item {
				if index_right != i {
					return []int{i, index_right}
				}
			}
		}
	}
	return []int{}
}
