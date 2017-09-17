package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	x := []int32{5, 3, 9, 2, 12, 3, 3, 3, 3, 12, 2, 3, 2, 3, 5, 9, 5, 2, 12, 12,
		12, 12, 5, 7, 2, 3, 3, 5, 7, 9, 9, 5, 12, 9, 5, 2, 3, 5, 12, 3,
		9, 9, 9, 2, 12, 3, 2, 12, 3, 5, 12, 3, 3, 9, 5, 2, 9, 12, 9, 9,
		3, 12, 2, 12, 5, 3, 12, 12, 3, 2, 2, 12, 9, 7, 3, 9, 5, 5, 9, 3,
		3, 9, 12, 9, 5, 5, 3, 9, 5, 9, 9, 7, 3, 2, 7, 3, 3, 9, 7, 5}

	y := map[int32]float64{2: 0.1, 3: 0.2, 5: 0.15, 7: 0.05, 9: 0.3, 12: 0.2}

	fmt.Println(x, y)

	
	f, _ := os.Open("lab1_range.txt")
	defer f.Close()
	scan := bufio.NewScanner(f)
	for scan.Scan() {
		fmt.Println(scan.Text())
	}

}
