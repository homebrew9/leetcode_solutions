package main

import "fmt"

func nextPermutation(nums []int)  {
    // Narayan Pandita's algorithm. See TAOCP Volume 4A.
    N := len(nums)
    i := 0
    for ind := 0; ind < N-1; ind++ {
        if nums[ind] < nums[ind+1] {
            i = ind
        }
    }
    j := i
    for ind := j; ind < N; ind++ {
        if nums[ind] > nums[i] {
            j = ind
        }
    }
    nums[i], nums[j] = nums[j], nums[i]
    if i != j {
        i++
    }
    j = N - 1
    for i < j {
        nums[i], nums[j] = nums[j], nums[i]
        i++
        j--
    }
    fmt.Printf("nums = %v\n", nums)
}

func nextPermutation_1(nums []int)  {
    // Narayan Pandita's algorithm. See TAOCP Volume 4A.
    N := len(nums)
    i := N - 2
    for ; i >= 0 && nums[i] >= nums[i+1]; i-- {
    }
    if i >= 0 {
        j := N - 1
        for ; j >= 0 && nums[j] <= nums[i]; j-- {
        }
        nums[i], nums[j] = nums[j], nums[i]
    }
    p, q := i + 1, N - 1
    for ; p < q; p, q = p + 1, q - 1 {
        nums[p], nums[q] = nums[q], nums[p]
    }
    fmt.Printf("nums = %v\n", nums)
}

func main() {
    data := [][]int{
            []int{1,2,3},
            []int{3,2,1},
            []int{1,1,5},
            []int{1,2,3,4,3,2,1},
            []int{1,4,1,8,3,1,1},
            []int{5,5,7,5,6,7,0,9,3,6,6,4,0,6,3,9,8,7,6,5},
            []int{5,1,2,1,5,4,0,3,5,1,0,9,0,2,4,8,3,1,9,6,3,9,0,7,5,7,6,6,7,8,6,4,4,0,3,7,2,6,2,0,7,6,6,2,4,8,4,9,7,7},
    }
    for _, nums := range data {
        fmt.Printf("nums = %v\n", nums)
        //nextPermutation(nums)
        nextPermutation_1(nums)
        fmt.Println("========================")
    }
}


/*

// 1. Search max j: nums[j] > nums[j-1]
// 2. Search max l: l >= j && nums[l] > nums[j-1]
// 3. Swap nums[j-1], nums[l]
// 4. Reverse nums[j:]
// For example:
// 123654 -> 124653 -> 124356
func nextPermutation(nums []int) {
    j := len(nums) - 1
    for ; j > 0 && nums[j-1] >= nums[j]; j-- {
    }
    if j != 0 {
        l := len(nums) - 1
        for ; l > j-1 && nums[j-1] >= nums[l]; l-- {
        }
        nums[j-1], nums[l] = nums[l], nums[j-1]
    }
    for k := len(nums) - 1; j < k; j, k = j+1, k-1 {
        nums[j], nums[k] = nums[k], nums[j]
    }
}

*/


