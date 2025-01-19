package main

import (
        "fmt"
)

func max(a, b int) int {
        if a > b {
                return a
        }
        return b
}

func min(a, b int) int {
        if a < b {
                return a
        }
        return b
}

func trap(height []int) int {
        N := len(height)
        var maxLeft = make([]int, N)
        var maxRight = make([]int, N)
        maxSoFar := 0
        for i := 1; i < N; i++ {
                maxSoFar = max(maxSoFar, height[i-1])
                maxLeft[i] = maxSoFar
        }
        maxSoFar = 0
        for i := N-2; i >= 0; i-- {
                maxSoFar = max(maxSoFar, height[i+1])
                maxRight[i] = maxSoFar
        }
        //fmt.Println(maxLeft)
        //fmt.Println(maxRight)
        res := 0
        for i := 1; i < N-1; i++ {
                curr := min(maxLeft[i], maxRight[i]) - height[i]
                if curr > 0 {
                        res += curr
                }
                //fmt.Printf("\ti, curr, res = %d, %d, %d\n", i, curr, res)
        }
        return res
}

func main() {
    arr := [][]int {
               []int {0,1,0,2,1,0,1,3,2,1,2,1},
               []int {4,2,0,3,2,5},
               []int {5,0,3,4,1,9},
           }
    for _, height := range arr {
        fmt.Printf("height = %v\n", height)
        r := trap(height)
        fmt.Printf("r = %d\n", r)
        fmt.Println("=================")
    }
}

