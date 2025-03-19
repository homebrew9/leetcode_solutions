package main

import "fmt"

func reinitializePermutation(n int) int {
	var perm, arr []int
	for i := 0; i < n; i++ {
		perm = append(perm, i)
		arr = append(arr, i)
	}
	steps := 0
	for true {
		tmp := make([]int, n)
		for i := 0; i < n; i++ {
			if i%2 == 0 {
				tmp[i] = arr[i/2]
			} else {
				tmp[i] = arr[n/2+(i-1)/2]
			}
		}
		copy(arr, tmp)
		steps++
		if areEqual(arr, perm) {
			return steps
		}
	}
	return 0
}

func areEqual(arr1, arr2 []int) bool {
	N, M := len(arr1), len(arr2)
	if N != M {
		return false
	}
	for i := 0; i < N; i++ {
		if arr1[i] != arr2[i] {
			return false
		}
	}
	return true
}

func main() {
	data := []int{
                       2,
                       4,
                       6,
                       8,
                      10,
                      72,
                     100,
                     598,
                     900,
                    1000,
	        }
	for _, n := range data {
		fmt.Printf("n = %d\n", n)
		r := reinitializePermutation(n)
		fmt.Printf("r = %d\n", r)
		fmt.Println("========================")
	}
}

