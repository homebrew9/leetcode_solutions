package main

import (
    "fmt"
    "math"
)

func numberOfStores(maxPerStore int, quantities []int) int {
    res := 0.0
    for _, v := range quantities {
        res += math.Ceil(float64(v) / float64(maxPerStore))
    }
    return int(res)
}

func minimizedMaximum(n int, quantities []int) int {
    left, right := 1, 100000
    for left <= right {
        mid := int((left + right) / 2)
        val := numberOfStores(mid, quantities)
        if val <= n {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return left
}

func main() {
    type Pair struct {
        n int
        quantities []int
    }
    data := []Pair{
                Pair {6, []int{11,6}},
                Pair {7, []int{15,10,10}},
                Pair {1, []int{100000}},
                Pair {14, []int{1,2,3,3,4,4,6,7,8,9}},
            }
    for _, v := range data {
        n, quantities := v.n, v.quantities
        fmt.Printf("n = %d, quantities = %v\n", n, quantities)
        r := minimizedMaximum(n, quantities)
        fmt.Printf("r = %d\n", r)
        fmt.Println("========================")
    }
}


