package main

import "fmt"

func trap(height []int) int {
    N := len(height)
    left_max := make([]int, N)
    right_max := make([]int, N)
    for i := 0; i < N; i++ {
        if i == 0 {
            left_max[i] = height[i]
        } else {
            left_max[i] = max(height[i-1], left_max[i-1])
        }
    }
    for i := N - 1; i >= 0; i-- {
        if i == N-1 {
            right_max[i] = height[i]
        } else {
            right_max[i] = max(height[i+1], right_max[i+1])
        }
    }
    res := 0
    for i := 1; i < N-1; i++ {
        water := min(left_max[i], right_max[i]) - height[i]
        if water > 0 {
            res += water
        }
    }
    return res
}

func main() {
    height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
    r := trap(height)
    fmt.Println(r)
}

