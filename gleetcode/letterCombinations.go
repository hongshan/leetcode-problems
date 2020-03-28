package gleetcode

func LetterCombinations(digits string) []string {
	if len(digits) < 1 {
		return []string{}
	}
	all := *getNumStrings(digits)
	left := &all[0]
	for i := 1; i < len(all); i++ {
		left = join(left, &all[i])
	}
	return *left
}
func join(left *[]string, right *[]string) *[]string {
	result := new([]string)
	for _, v := range *left {
		for _, v1 := range *right {
			*result = append(*result, v+v1)
		}
	}
	return result
}
func getNumStrings(digits string) *[][]string {
	ret := new([][]string)
	num_map := make(map[string][]string)
	num_map["2"] = []string{"a", "b", "c"}
	num_map["3"] = []string{"d", "e", "f"}
	num_map["4"] = []string{"g", "h", "i"}
	num_map["5"] = []string{"j", "k", "l"}
	num_map["6"] = []string{"m", "n", "o"}
	num_map["7"] = []string{"p", "q", "r", "s"}
	num_map["8"] = []string{"t", "u", "v"}
	num_map["9"] = []string{"w", "x", "y", "z"}
	for _, v := range digits {
		*ret = append(*ret, num_map[string(v)])
	}
	return ret
}
