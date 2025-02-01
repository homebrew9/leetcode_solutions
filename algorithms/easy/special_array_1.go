package main

import "fmt"

func isArraySpecial(nums []int) bool {
    for i := 1; i < len(nums); i++ {
        if (nums[i-1] & 1) == (nums[i] & 1) {
            return false
        }
    }
    return true
}

func main() {
    data := [][]int{
                []int{1},
                []int{2,1,4},
                []int{4,3,1,6},
            }
    for _, nums := range data {
        fmt.Printf("nums = %v\n", nums)
        r := isArraySpecial(nums)
        fmt.Printf("r = %v\n", r)
        fmt.Println("=================")
    }
}


