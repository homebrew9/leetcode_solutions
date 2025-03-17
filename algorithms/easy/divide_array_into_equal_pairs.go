package main

import "fmt"

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

func main() {
    data := [][]int {
                []int{3,2,3,2,2,2},
                []int{1,2,3,4},
            }
	for _, nums := range data {
		fmt.Printf("nums = %v\n", nums)
		r := divideArray(nums)
		fmt.Printf("r = %v\n", r)
		fmt.Println("======================")
	}
}

