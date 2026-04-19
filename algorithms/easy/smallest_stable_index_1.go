package main

import "fmt"

func firstStableIndex(nums []int, k int) int {
	N := len(nums)
	lpfx := make([]int, N)
	copy(lpfx, nums)
	for i := 0; i < N; i++ {
		if i == 0 {
			lpfx[i] = nums[i]
		} else {
			lpfx[i] = max(lpfx[i-1], nums[i])
		}
	}
	rpfx := make([]int, N)
	copy(rpfx, nums)
	for i := N - 1; i >= 0; i-- {
		if i == N-1 {
			rpfx[i] = nums[i]
		} else {
			rpfx[i] = min(rpfx[i+1], nums[i])
		}
	}
	for i := 0; i < N; i++ {
		if lpfx[i]-rpfx[i] <= k {
			return i
		}
	}
	return -1
}

func main() {
	type Pair struct {
		nums []int
		k    int
	}
	for _, v := range []Pair{Pair{[]int{5, 0, 1, 4}, 3},
		Pair{[]int{3, 2, 1}, 1},
		Pair{[]int{0}, 0},
	} {
		fmt.Printf("nums = %v ; k = %d\n", v.nums, v.k)
		r := firstStableIndex(v.nums, v.k)
		fmt.Printf("r = %d\n", r)
		fmt.Println("===================")
	}
}





