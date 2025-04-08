package main

import "fmt"

func minimumOperations(nums []int) int {
	seen := make(map[int]bool)
	i := len(nums) - 1
	for i >= 0 {
		ok, _ := seen[nums[i]]
		if ok {
			break
		}
		seen[nums[i]] = true
		i--
	}
	return (i + 3) / 3
}

func main() {
	data := [][]int{
		[]int{1, 2, 3, 4, 2, 3, 3, 5, 7},
		[]int{4, 5, 6, 4, 4},
		[]int{6, 7, 8, 9},
	}
	for _, nums := range data {
		fmt.Printf("nums = %v\n", nums)
		r := minimumOperations(nums)
		fmt.Printf("r = %d\n", r)
		fmt.Println("====================")
	}
}
