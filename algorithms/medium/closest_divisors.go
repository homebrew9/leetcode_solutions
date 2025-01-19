package main

import (
    "fmt"
    "math"
)

func closestDivisors(num int) []int {
    i := int(math.Sqrt(float64(num+2)))
    for i > 0 {
        if (num+1) % i == 0 {
            return []int{i, (num+1)/i}
        }
        if (num+2) % i == 0 {
            return []int{i, (num+2)/i}
        }
        i--
    }
    return []int{}
}

func main() {
    data := []int{
                8,
                123,
                999,
                2,
                1,
            }
    for _, num := range data {
        fmt.Printf("num = %d\n", num)
        r := closestDivisors(num)
        fmt.Printf("r   = %v\n", r)
        fmt.Println("===============")
    }
}

