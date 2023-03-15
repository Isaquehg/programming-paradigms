package main

import(
	"fmt"
	"math"
	"math/rand"
)

func main(){
	//initialization
	var a float64
	var b float64
	var c float64
	var delta float64
	var x1 float64
	var x2 float64
	var continuar bool = true

	for continuar{
		//input
		fmt.Scan(&a)
		fmt.Scan(&b)
		fmt.Scan(&c)

		//delta
		delta = (b * b) - (4 * a * c)

		//x1 & x2
		x1 = (-(b) + math.Sqrt(delta)) / (2 * a)
		x2 = (-(b) - math.Sqrt(delta)) / (2 * a)

		//output
		fmt.Println(x1)
		fmt.Println(x2)

		fmt.Scan(&continuar)
	}

	//array
	/*
	arr1 := [5]int{}
	arr2 := [...]int{1, 2}
	arr3 := [5]int{1, 2, 3, 4}
	*/
	//ex 2
	rand_num := [100]int{}

	for i := 0; i < 100; i ++ {
		rand_num[i] = rand.Intn(100)
	}

	for i := 0; i < 100; i ++ {
		if rand_num[i] % 2 == 0 {
			print(rand_num[i])
		}
	}

	
}