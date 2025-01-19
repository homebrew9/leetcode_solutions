//
// Step 1: Remove all valid brackets as much as possible.
// Step 2: We will be left with this pattern: '].....][.....[' where each bracket has
//         a frequency of n. That's because the string is guaranteed to be valid.
// Step 3: The answer is ceiling(len(s)/4). Try it out for a few test cases.
//

package main

import "fmt"

func minSwaps(s string) int {
    stack := []rune{}
    for _, v := range s {
        if v == ']' && len(stack) > 0 && stack[len(stack)-1] == '[' {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, v)
        }
    }
    return int(float64(len(stack)) / 4 + 0.5)
}

func main() {
    for _, s := range []string {
                          "][][",
                          "]]][[[",
                          "[]",
                          "]][]]][][[][[[]][[",
                          "][",
                          "[]][[]]]]][]][[]][][[[][[]][]]]][[[]][][][[]][]]]]]]]]]][[[[[[[[]]]]]][][[[][]][]][[][[[[]]][][[[[][[[[[[[",
                }{
        fmt.Printf("s = %s\n", s)
        r := minSwaps(s)
        fmt.Printf("r = %d\n", r)
        fmt.Println("==========================")
    }
}


