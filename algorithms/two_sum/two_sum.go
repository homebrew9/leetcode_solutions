/*
Given an array of integers "num" and an integer "target", return indices of
two numbers such that they add up to "target". You may assume that each input
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
*/
package main

import (
    "fmt"
)

func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    var arr []int
    for i, v := range nums {
        if _, ok := seen[target - v]; ok {
            arr = append(arr, i, seen[target - v])
            break
        }
        seen[v] = i
    }
    return arr
}

func main() {
    arr1 := []int{2,7,11,15}
    fmt.Println(twoSum(arr1, 9))

    arr2 := []int{3,2,4}
    fmt.Println(twoSum(arr2, 6))

    arr3 := []int{3,3}
    fmt.Println(twoSum(arr3, 6))
}

