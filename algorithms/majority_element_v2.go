package main

import "fmt"

func majorityElement(nums []int) int {
    // Boyer Moore voting algorithm
    if len(nums) == 1 {
        return nums[0]
    }
    // (A) Voting phase
    var major_element int
    majority := len(nums)/2
    count := 0
    for i, v := range nums {
        //fmt.Printf("\t>>> Now processing: [%d]\n", v)
        if i == 0 || count == 0 { 
            major_element = v
            count = 1
        } else if v == major_element {
            count++
        } else {
            count--
        }
        //fmt.Printf("\t\t>>> major_element, count = [%d], [%d]\n", major_element, count)
    }
    // (B) Verification phase
    count = 0
    for _, v := range nums {
        if v == major_element {
            count++
        }
    }
    if count <= majority {
        major_element = -1
    }
    return major_element
}

func main() {
    arr := [][]int{
               []int{3,3,5,7,5,7,3,5,7},
               []int{1,2,1,3,1,2,1,1,4,1,4,2,1,3,1,1,3,1,4,2,1,1}, // Y,G,Y,R,Y,G,Y,Y,B,Y,B,G,Y,R,Y,Y,R,Y,B,G,Y,Y
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


