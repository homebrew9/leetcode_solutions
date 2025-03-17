package main

import (
          "fmt"
          "sort"
       )

func divideArray(nums []int) bool {
    hsh := make(map[int]int)
    for _, n := range nums {
        _, ok := hsh[n]
        if ok {
            delete(hsh, n)
        } else {
            hsh[n]++
        }
    }
    return len(hsh) == 0
}

func divideArray_1(nums []int) bool {
    hsh := make(map[int]int)
    for _, v := range nums {
        hsh[v]++
    }
    for _, v := range hsh {
        if v % 2 == 1 {
            return false
        }
    }
    return true
}

func divideArray_2(nums []int) bool {
    N := len(nums)
    sort.Ints(nums)
    for i := 0; i < N; i += 2 {
        if nums[i] != nums[i+1] {
            return false
        }
    }
    return true
}

func main() {
    data := [][]int {
                []int{3,2,3,2,2,2},
                []int{1,2,3,4},
            }
    for _, nums := range data {
        fmt.Printf("nums = %v\n", nums)
        r := divideArray(nums)
        r1 := divideArray_1(nums)
        r2 := divideArray_2(nums)
        fmt.Printf("r  = %v\n", r)
        fmt.Printf("r1 = %v\n", r1)
        fmt.Printf("r2 = %v\n", r2)
        fmt.Println("======================")
    }
}

