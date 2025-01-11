package main

import (
    "fmt"
)

func removeElement(nums []int, val int) int {
    i := 0
    for _, v := range nums {
        if v != val {
            nums[i] = v
            i++
        }
    }
    fmt.Printf("\t==> nums = %v\n", nums)
    return i
}

// Main section
func main() {
    type Pair struct {
        nums []int
        val  int
    }
    for _, v := range []Pair{
        Pair{[]int{1, 2, 2, 3, 4, 4, 5, 2, 2, 2, 6, 7, 4, 8}, 2},
        Pair{[]int{1, 2, 2, 3, 4, 4, 5, 2, 2, 2, 6, 7, 4, 8}, 4},
        Pair{[]int{1, 2, 2, 3, 4, 4, 5, 2, 2, 2, 6, 7, 4, 8}, 9},
        Pair{[]int{1, 2, 2, 3}, 2},
    } {
        fmt.Printf("nums, val = %v, %d\n", v.nums, v.val)
        r := removeElement(v.nums, v.val)
        fmt.Printf("r = %d\n", r)
        fmt.Println("======================")
    }
}

