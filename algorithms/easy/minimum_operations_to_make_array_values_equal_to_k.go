package main

import "fmt"

func minOperations(nums []int, k int) int {
	freq := make(map[int]int)
	for _, n := range nums {
		freq[n]++
	}
	res := 0
	for key, _ := range freq {
		if key > k {
			res++
		}
		if key < k {
			return -1
		}
	}
	return res
}

func main() {
	type Pair struct {
		nums []int
		k    int
	}
	for _, v := range []Pair{Pair{[]int{5, 2, 5, 4, 5}, 2},
		Pair{[]int{2, 1, 2}, 2},
		Pair{[]int{9, 7, 5, 3}, 1},
	} {
		fmt.Printf("nums, k = %v, %d\n", v.nums, v.k)
		r := minOperations(v.nums, v.k)
		fmt.Printf("r = %d\n", r)
		fmt.Println("=======================")

	}
}
