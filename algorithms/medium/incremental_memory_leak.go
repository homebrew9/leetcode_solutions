package main

import "fmt"

func memLeak(memory1 int, memory2 int) []int {
    i := 0
    for true {
        i++
        if memory1 < i && memory2 < i {
            return []int{i, memory1, memory2}
        }
        if memory1 >= memory2 {
            memory1 -= i
        } else {
            memory2 -= i
        }
    }
    return []int{}
}

func main() {
    data := [][]int{
        []int{2, 2},
        []int{8, 11},
        []int{1234567890, 2147483647},
        []int{0, 0},
        []int{0, 10},
    }
    for _, arr := range data {
        memory1, memory2 := arr[0], arr[1]
        fmt.Println(memory1, memory2)
        r := memLeak(memory1, memory2)
        fmt.Println(r)
        fmt.Println("===================")
    }
}


