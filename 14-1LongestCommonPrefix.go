package main

import (
	"fmt"
	// "strconv"
)

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	cols := [][]byte{}
	min_len := int(^uint(0) >> 1)
	// get min len of every row O(n)
	for _, v := range strs {
		if l := len(v); l < min_len {
			min_len = l
		}
	}

	// 构造每一行的同一列组成矩阵 min_len是常数， O(n) * min_len = O(n)
	for i := 0; i < len(strs); i++ {
		for j := 0; j < min_len; j++ {
			if len(cols) <= j {
				cols = append(cols, []byte{})
			}
			cols[j] = append(cols[j], strs[i][j])
		}
	}
	// 判断构造的矩阵的row里面所有的byte是不是相同 O(n)
	end := min_len
	for k, v := range cols {
		same := func(first byte, array []byte) bool {
			ret := byte('0')
			for _, v := range array {
				ret += first ^ v
			}
			return ret == '0'
		}(v[0], v)
		if !same {
			end = k
			break
		}
	}
	return strs[0][0:end]
}
func main() {
	fmt.Println(longestCommonPrefix([]string{"hello7", "hell343434", "hello344"}))
	fmt.Println(longestCommonPrefix([]string{""}))
	fmt.Println(longestCommonPrefix([]string{}))
}
