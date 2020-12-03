package main

import (
    "bufio"
    "fmt"
    "log"
	"os"
	"strings"
	"strconv"
)

func check_counts(min_, max_ int, pwd, letter string) int{
	counted := strings.Count(pwd, letter)
	if (counted >= min_ && counted<=max_){
		return 1
	}
	return 0
}

func check_positions(min_, max_ int, pwd, letter string) int{
	if (strings.Split(pwd, "")[min_-1]==letter || strings.Split(pwd, "")[max_-1]==letter) && !(strings.Split(pwd, "")[min_-1]==letter && strings.Split(pwd, "")[max_-1]==letter){
		return 1
	}
	return 0
}

func split_to_parts(line string) (int,int){
	s := strings.Split(line, " ")
	min_, err := strconv.Atoi(strings.Split(s[0], "-")[0])
	max_, err := strconv.Atoi(strings.Split(s[0], "-")[1])
	letter := strings.Split(s[1], ":")[0]
	pwd := s[2]
	if err != nil{
	}
	v := check_counts(min_, max_, pwd, letter)
	w := check_positions(min_, max_, pwd, letter)
	return v, w
}

func main() {
    file, err := os.Open("day2_input.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
	
	current_count := 0
	current_count_2 := 0

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
		text := scanner.Text()
		v, w := split_to_parts(text)
		current_count = current_count + v 
		current_count_2 = current_count_2 + w

    }
	fmt.Println(current_count)
	fmt.Println(current_count_2)
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}