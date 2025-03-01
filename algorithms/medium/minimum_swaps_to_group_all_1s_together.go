package main

import (
	"fmt"
    "math"
)

func minSwaps(data []int) int {
    size := 0
    for _, v := range data {
        if v == 1 {
            size++
        }
    }
    N := len(data)
    zeroCount := 0
    res := math.MaxInt
    for i := 0; i < N; i++ {
        if i < size {
            if data[i] == 0 {
                zeroCount++
            }
        } else {
            res = min(res, zeroCount)
            if data[i - size] == 0 {
                zeroCount--
            }
            if data[i] == 0 {
                zeroCount++
            }
        }
    }
    res = min(res, zeroCount)
    return res
}

func main() {
	lists := [][]int{
                 []int{1,0,1,0,1},
                 []int{0,0,0,1,0},
                 []int{1,0,1,0,1,0,0,1,1,0,1},
                 []int{0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0},
	}
	for _, data := range lists {
		fmt.Printf("data = %v\n", data)
	    r := minSwaps(data)
        fmt.Printf("r = %d\n", r)
		fmt.Println("===========================")
	}
}

