package main

import (
	"fmt";
  "math"
)

func exerc2() {
	var a float64
	var b float64
	var c float64
	var delta float64
  var stop int = 0;

  for stop==0 {
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

  	fmt.Print("Continuar (0-continuar, 1-parar): ")
  	fmt.Scan(&stop)
  }
}
