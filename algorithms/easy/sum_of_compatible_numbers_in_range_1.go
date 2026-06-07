package main

import "fmt"

func sumOfGoodIntegers(n int, k int) int {
	res := 0
	for x := max(1, n-k); x <= n+k; x++ {
		if n&x == 0 {
			res += x
		}
	}
	return res
}

func main() {
	type Pair struct {
		n int
		k int
	}
	for _, v := range []Pair{
		{2, 3},
		{5, 1},
		{4, 9},
		{17, 83},
	} {
		fmt.Printf("n = %d ; k = %d\n", v.n, v.k)
		r := sumOfGoodIntegers(v.n, v.k)
		fmt.Printf("r = %d\n", r)
		fmt.Println("===================")
	}
}


