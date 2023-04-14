package main

import (
	"fmt"
	"math/rand"
)

func exerc3() {
  var pares int = 0
	arr := [10]int{}

  for index,_ := range arr {
    arr[index] = rand.Intn(100)
    fmt.Println(arr[index])
  }

  for _,element := range arr {
    if element%2 == 0{
      pares++
    }
  }

  fmt.Println("Pares: ", pares)
}
