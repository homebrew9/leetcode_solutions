package main
import "fmt"

func maxSubArray(nums []int) int {
    // Kadane's algorithm
    // If the current (running) sum is less than current element, then
    // set the current sum to the current element. The maxSum is set to
    // the higher of maxSum and current sum at each iteration.
    currSum := 0
    maxSum := nums[0]
    for _, v := range nums {
        currSum += v
        if v > currSum {
            currSum = v
        }
        if currSum > maxSum {
            maxSum = currSum
        }
    }
    return maxSum
}

func main() {
    arr := [][]int {
               []int{-2, 1, -3, 4, -1, 2, 1, -5, 4},
               []int{1, 2, 3, 4, 5},
               []int{-1, -2, -3, -4, -5},
               []int{5, 4, -1, 7, 8},
               []int{1, -1, 1, -1, 1, -1},
               []int{1, -1},
               []int{1},
               []int{1, 2, 3, -1, -2, -3},
               []int{1, 1, 1, 1, 1, 1, 1},
           }
    for _, v := range arr {
        fmt.Println("nums           = ", v)
        fmt.Println("maxSubArray    = ", maxSubArray(v))
        fmt.Println("==========================")
    }
}

