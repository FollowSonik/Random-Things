package main

import "fmt"

func main() {
	hanoi(19, 1, 2)
}

func hanoi(n int, i int, k int) {
	if n == 1 {
		fmt.Printf("Move dist %d from pin %d to %d\n", n, i, k)
	} else {
		var tmp = 6 - i - k
		hanoi(n-1, i, tmp)
		fmt.Printf("Move disk %d from pin %d to %d\n", n, i, k)
		hanoi(n-1, tmp, k)
	}
}
