package main

import "fmt"

//func generate(numRows int) [][]int {
//    pt := make([][]int, numRows)
//    pascal := make([][]int, numRows)
//    for r := 0; r < numRows; r++  {
//        //fmt.Println(r)
//        pascal[r] = make([]int, numRows)
//        for c := 0; c < numRows-r; c++ {
//            if r == 0 || c == 0 {
//                pascal[r][c] = 1 
//            } else {
//                pascal[r][c] = pascal[r][c-1] + pascal[r-1][c]
//            }
//        }
//    }
//    //fmt.Println(pascal)
//    //pt := make([][]int, numRows)
//    for r := 0; r < numRows; r++ {
//        pt[r] = make([]int, r+1)
//        for c := 0; c < r+1; c++ {
//            pt[r][c] = pascal[r-c][c]
//        }
//    }
//    return pt
//}

func generate(numRows int) [][]int {
    pt := make([][]int, numRows)
    for r := 0; r < numRows; r++ {
        pt[r] = make([]int, r+1)
        pt[r][0] = 1
        for c := 1; c < r; c++ {
            pt[r][c] = pt[r-1][c-1] + pt[r-1][c]
        }
        pt[r][r] = 1
    }
    return pt
}



func main() {
    arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30}
    //arr := []int{1}
    for _, v := range arr {
        fmt.Printf("numRows = %d\n", v)
        r := generate(v)
        fmt.Println(r)
        fmt.Println("=====================================")
    }
}


