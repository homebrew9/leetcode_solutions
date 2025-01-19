package main

import (
    "container/heap"
    "math"
    "fmt"
)

// An IntHeap is a max-heap of ints. Notice the change in the "Less" function.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
    // Push and Pop use pointer receivers because they modify the slice's length,
    // not just its contents.
    *h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func pickGifts(gifts []int, k int) int64 {
    h := &IntHeap{}
    heap.Init(h)
    for _, v := range gifts {
        heap.Push(h, v)
    }
    for k > 0 {
        heap.Push(h, int(math.Sqrt(float64(heap.Pop(h).(int)))))
        k--
    }
    res := int64(0)
    for h.Len() > 0 {
        res += int64(h.Pop().(int))
    }
    return res
}

func main() {
    type Pair struct {
        gifts []int 
        k     int
    }
    for _, v := range []Pair { Pair{[]int{25,64,9,4,100}, 4},
                               Pair{[]int{1,1,1,1}, 4},
                               Pair{[]int{38,73,86,77,21,10,78,83,17,10,33,88,56,14,4,74,32,57,100,10,12,92,73,55,47,91,3,68,29,64,62,19,8,87,34,74,37,72,94,9,57,59,73,90,33,20,16,5,64,85,11,76,93,35,93,23,17,21,48,35}, 29},
                             }{
        fmt.Printf("gifts = %v ; k = %d\n", v.gifts, v.k)
        r := pickGifts(v.gifts, v.k)
        fmt.Printf("r = %d\n", r)
        fmt.Println("===================")
    }
}


