//
// I am unable to make it work. Not sure why the map does not get cleared!
//
package main

import "fmt"

var res int

func totalNQueens(n int) int {
    res = 0
    r := 0
    cset := make(map[int]bool)
    dset := make(map[int]bool)
    adset := make(map[int]bool)
    backtrack(r, n, cset, dset, adset)
    return res
}

func backtrack(r, n int, cset, dset, adset map[int]bool) bool {
    //fmt.Println(r, n, cset, dset, adset)
    if r == n {
        res++
        return true
    }
    for c := 0; c < n; c++ {
        // pos = (r, c)
        _, ok := cset[c]; if ok {continue}
        _, ok = dset[r - c]; if ok {continue}
        _, ok = adset[r + c]; if ok {continue}
        cset[c] = true
        dset[r - c] = true
        adset[r + c] = true
        res := backtrack(r + 1, n, cset, dset, adset)
        if !res {
            delete(cset, c)
            delete(dset, r - c)
            delete(adset, r + c)
        }
    }
    return false
}

func main() {
    data := []int{1,2,3,4,5,6,7,8,9}
    for _, n := range data {
        fmt.Printf("n = %d\n", n)
        totalNQueens(n)
        fmt.Printf("res = %d\n", res)
        fmt.Println("====================")
    }
}


