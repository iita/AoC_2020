package main

import (
    "fmt"
    "io/ioutil"
    "log"
)

func 


func main() {
    content, err := ioutil.ReadFile("day4_input.txt")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(content))
}