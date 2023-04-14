package main

import (
	"fmt";
  "math"
)

func exerc1() {
	var a = 3.0
	var b = 3.0
	var c = 3.0
	var delta = 3.0

	fmt.Print("A: ")
	fmt.Scan(&a)
	fmt.Print("B: ")
	fmt.Scan(&b)
	fmt.Print("C: ")
	fmt.Scan(&c)

	delta = b*b - 4*a*c

  if delta<0 {
    fmt.Println("Sem raizes reais!")
  } else if delta==0 {
    fmt.Println("Raízes iguais de valor: ", (-b+math.Sqrt(delta))/(2*a)) 
  } else {
    fmt.Println("Raíz 1: ", (-b+math.Sqrt(delta))/(2*a)) 
    fmt.Println("Raíz 2: ", (-b-math.Sqrt(delta))/(2*a)) 
  }
    
	fmt.Print(delta)
}
