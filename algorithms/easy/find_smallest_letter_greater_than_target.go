package main
import (
    "fmt"
)

func nextGreatestLetter(letters []byte, target byte) byte {
    for _, v := range(letters) {
        if v > target {
            return v
        }
    }
    return letters[0]
}

func main() {
    type Pair struct {
        lst []byte 
        tgt byte
    }
    for _, v := range []Pair { Pair{[]byte{'c','d','f'}, 'e'},
                               Pair{[]byte{'a','b','c'}, 'q'},
                               Pair{[]byte{'m','s','y'}, 'z'},
                             }{
        fmt.Printf("letters = %v ; target = %c\n", string(v.lst[:]), v.tgt)
        r := nextGreatestLetter(v.lst, v.tgt)
        fmt.Printf("r = %c\n", r)
        fmt.Println("===================")
    }
}

