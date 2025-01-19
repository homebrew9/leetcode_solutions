package main

import "fmt"

func decrypt(code []int, k int) []int {
    N := len(code)
    res := make([]int, N)
    if k == 0 {
        return res
    }
    // code = [5,7,1,4        ] ; k = 3
    //  arr = [5,7,1,4,5,7,1,4]
    arr := make([]int, 2*N)
    copy(arr[:N], code)
    copy(arr[N:], code)
    sum := 0
    var p int
    if k < 0 {
        k = -k
        p = N - k
        for ; p < N; p++ {
            sum += arr[p]
        }
    } else {
        p = 1
        for ; p < 1 + k; p++ {
            sum += arr[p]
        }
    }
    for i := 0; i < N; i++ {
        if i > 0 {
            sum += arr[p] - arr[p - k]
            p++
        }
        res[i] = sum
    }
    return res
}

func main() {
    type Pair struct {
        code []int 
        k     int
    }
    for _, v := range []Pair {
                               Pair{[]int{5,7,1,4}, 3},
                               Pair{[]int{1,2,3,4}, 0},
                               Pair{[]int{2,4,9,3}, -2},
                               Pair{[]int{5,7,1,4}, -3},
                               Pair{[]int{38,73,86,77,21,10,78,83,17,10,33,88,56,14,4,74,32,57,100,10,12,92,73,55,47,91,3,68,29,64,62,19,8,87,34,74,37,72,94,9,57,59,73,90,33,20,16,5,64,85,11,76,93,35,93,23,17,21,48,35}, 29},
                             }{
        fmt.Printf("code = %v ; k = %d\n", v.code, v.k)
        r := decrypt(v.code, v.k)
        fmt.Printf("r = %d\n", r)
        fmt.Println("===================")
    }
}

