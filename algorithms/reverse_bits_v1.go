package main

import (
    "fmt"
)

func reverseBits(num uint32) uint32 {
    var ret uint32
    arr := make([]uint32, 32)
    i := 0
    for num > 0 {
        q := num / 2
        r := num % 2
        //fmt.Printf("\t>>> num, q, r = %9d, %9d, %9d", num, q, r)
        arr[i] = r
        i++
        num = q
    }
    //fmt.Println(arr)
    //fmt.Printf("\t>>> %032b => %d => %s\n", num, num, s)
    ret = 0
    pv := uint32(1)
    for i = 31; i >= 0; i-- {
        ret += arr[i] * pv
        pv *= 2
    }
    return ret
}

func main() {
    arr := []uint32{
               0b00000000000000000000000000000110,
               0b00000010100101000001111010011100,
               0b11111111111111111111111111111101,
           }
    for _, v := range arr {
        fmt.Printf("%032b => %d\n", v, v)
        ret := reverseBits(v)
        fmt.Printf("%032b => %d\n", ret, ret)
        fmt.Println("============================================================")
    }
}

