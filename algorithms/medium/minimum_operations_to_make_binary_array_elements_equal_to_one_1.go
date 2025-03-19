package main

import "fmt"

func minOperations(nums []int) int {
    N := len(nums)
    res := 0
    for i := 0; i < N - 2; i++ {
        if nums[i] == 0 {
            nums[i] = 1
            if nums[i+1] == 0 {
                nums[i+1] = 1
            } else {
                nums[i+1] = 0
            }
            if nums[i+2] == 0 {
                nums[i+2] = 1
            } else {
                nums[i+2] = 0
            }
            res++
        }
    }
    if nums[N-1] == 0 || nums[N-2] == 0 {
        return -1
    }
    return res
}

func main() {
	data := [][]int{
                 []int{0,1,1,1,0,0},
                 []int{0,1,1,1},
                 []int{0,0,0,0,0,0,0,0,0},
                 []int{1,1,1,1,1,1,1,1,1},
                 []int{1,0,0,0,1,0,0,0,1},
	        }
	for _, nums := range data {
		fmt.Printf("nums = %v\n", nums)
		r := minOperations(nums)
		fmt.Printf("r = %d\n", r)
		fmt.Println("==========================")
	}
}

