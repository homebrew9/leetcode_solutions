package main

import "fmt"

func majorityElement(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }
    var major_element int
    majority := len(nums)/2
    hsh := make(map[int]int)
    for _, v := range nums {
        count, ok := hsh[v]
        if !ok {
            hsh[v] = 1
        } else {
            hsh[v] = count + 1
            if hsh[v] > majority {
                major_element = v
                break
            }
        }
    }
    return major_element
}

func main() {
    arr := [][]int{
               []int{3,2,3},
               []int{2,2,1,1,1,2,2},
               []int{1},
               []int{2,2},
               []int{1,2,1},
           }
    for _, v := range arr {
        fmt.Println(v)
        r := majorityElement(v)
        fmt.Println(r)
        fmt.Println("===================================")
    }
}

