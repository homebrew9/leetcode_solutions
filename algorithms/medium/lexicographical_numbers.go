package main

import "fmt"

var res []int

func dfs(x, n int) {
    if x <= n {
        res = append(res, x)
        if x * 10 <= n {
            for y := 0; y < 10; y++ {
                t := 10 * x + y
                dfs(t, n)
            }
        }
    }
}

func lexicalOrder(n int) []int {
    res = res[:0]
    for i := 1; i < 10; i++ {
        dfs(i, n)
    }
    return res
}

func main() {
    data := []int{3, 2, 123, 1234}
    for _, n := range data {
        fmt.Println(n)
        fmt.Println(lexicalOrder(n))
        fmt.Println("==================")
    }
}

