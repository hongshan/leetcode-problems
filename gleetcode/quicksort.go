package gleetcode

// 第一次调用
// l是要排序的数组
// lo = 0
// hi = len(l) - 1
func QucikSort(l *[]int, lo int, hi int) {
	if lo < hi {
		p := partition(l, lo, hi)
		QucikSort(l, lo, p-1)
		QucikSort(l, p+1, hi)
	}
}

// p代表一个位置
// p左边都是比pivot小或者相等的 <=
// p右边都是比pivot大的 >
// partion的真正目的是找到pivot的位置
// 当pivot的位置正确之后，只需要递归lo 到 p-1 以及 p+1 到 hi

func partition(l *[]int, lo int, hi int) int {
	pivot := (*l)[hi]
	p := lo
	for j := lo; j < hi; j++ {
		if (*l)[j] <= pivot {
			(*l)[p], (*l)[j] = (*l)[j], (*l)[p]
			p = p + 1
		}
	}
	(*l)[p], (*l)[hi] = (*l)[hi], (*l)[p]
	return p
}
