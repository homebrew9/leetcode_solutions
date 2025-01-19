package main

import (
    "fmt"
    "strconv"
)

func solve(expression string, i, j int) []int {
    n, err := strconv.Atoi(expression[i : j+1])
    if err == nil {
        return []int{n}
    }
    arr := []int{}
    for k := i; k < j+1; k++ {
        n, err = strconv.Atoi(string(expression[k]))
        if err != nil {
            op := expression[k]
            leftArr := solve(expression, i, k-1)
            rightArr := solve(expression, k+1, j)
            for _, lv := range leftArr {
                for _, rv := range rightArr {
                    if op == '+' {
                        arr = append(arr, lv+rv)
                    } else if op == '-' {
                        arr = append(arr, lv-rv)
                    } else if op == '*' {
                        arr = append(arr, lv*rv)
                    }
                }
            }
        }
    }
    return arr
}

func diffWaysToCompute(expression string) []int {
    N := len(expression)
    i, j := 0, N-1
    results := solve(expression, i, j)
    return results
}

func main() {
    data := []string{
        "2-1-1",
        "2*3-4*5",
        "2*7+3",
        "2*3-4+5+6*7-8*9+1",
        "1+2-3*4+5-6*7+8-9*10",
        "17+37*53-79+83*91-97",
        "98",
        "98-98",
    }
    for _, expression := range data {
        r := diffWaysToCompute(expression)
        fmt.Println(expression)
        fmt.Println(r)
        fmt.Println("=======================")
    }
}

