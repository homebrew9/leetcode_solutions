package main

import "fmt"

func twoSumRec(nums []int, tgt int, lo int, hi int) []int {
    sum := nums[lo] + nums[hi]
    if sum == tgt {
        return []int{lo+1, hi+1}
    }
    if sum < tgt {
        return twoSumRec(nums, tgt, lo+1, hi)
    }
    return twoSumRec(nums, tgt, lo, hi-1)
}

func twoSum(numbers []int, target int) []int {
    left, right := 0, len(numbers)-1
    ret := twoSumRec(numbers, target, left, right)
    return ret
}

func main() {
    // The first element is the target, the rest form the "numbers" array
    arr := [][]int{
               []int{19, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10},
               []int{18, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10},
               []int{6, 1, 5, 13, 31, 59, 73, 91},
               []int{92, 1, 5, 13, 31, 59, 73, 91},
               []int{132, 1, 5, 13, 31, 59, 73, 91},
               []int{44, 1, 5, 13, 31, 59, 73, 91},
               []int{96, 1, 5, 13, 31, 59, 73, 91},
               []int{3, 1, 2},
           }
    for _, v := range arr {
        target := v[0]
        numbers := v[1:]
        r := twoSum(numbers, target)
        fmt.Println(numbers)
        fmt.Println(target)
        fmt.Println(r)
        fmt.Println("==========================")
    }
}


