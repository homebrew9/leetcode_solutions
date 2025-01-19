package main

import "fmt"

func nextGreaterElement(nums1 []int, nums2 []int) []int {
    hsh := make(map[int]int)
    stack := []int{}
    for _, v := range nums2 {
        for len(stack) > 0 && stack[len(stack)-1] < v {
            hsh[stack[len(stack)-1]] = v
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, v)
    }
    for len(stack) > 0 {
        hsh[stack[len(stack)-1]] = -1
        stack = stack[:len(stack)-1]
    }
    res := []int{}
    for _, v := range nums1 {
        res = append(res, hsh[v])
    }
    return res
}

func main() {
    type Pair struct {
        nums1 []int
        nums2 []int
    }
    data := []Pair {
                Pair{[]int{4,1,2}, []int{1,3,4,2}},
                Pair{[]int{2,4}, []int{1,2,3,4}},
                Pair{[]int{0,15,9,22,1}, []int{2,9,1,4,15,3,22,0}},
            }
    for _, v := range data {
        nums1, nums2 := v.nums1, v.nums2
        fmt.Printf("nums1 = %v , nums2 = %v\n", nums1, nums2)
        r := nextGreaterElement(nums1, nums2)
        fmt.Printf("r = %v\n", r)
        fmt.Println("===============")
    }
}


