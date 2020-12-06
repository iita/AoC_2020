
package main

import (
    "bufio"
    "fmt"
    "log"
	"os"
)

func find_tree(line string, current_spot int, columns int, current_count int) (int,int){
    col_nr := current_spot % 31
    if string(line[col_nr]) == "#"{
        return current_count + 1, current_spot + columns
    }
    return current_count, current_spot + columns
}

func check_if_line_relevant(line_nr int, row_skip int) bool {
    if line_nr % row_skip == 0 {
        return true
    }
    return false
}

func check_all_lines(path string, row_skip int, columns int) (int) {
	file, err := os.Open(path)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
	trees_found := 0
	current_spot := 0
	line_nr := 0

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        text := scanner.Text()
        if check_if_line_relevant(line_nr, row_skip) {
			trees_found, current_spot = find_tree(text, current_spot, columns, trees_found)
		}
		line_nr++

	}
	if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
	return trees_found
}

func check_all_variations(path string) int{
	variations := [5][2]int{
		{1,1},
		{1,3},
		{1,5},
		{1,7},
		{2,1},
	}
	total := 1
	for _, variant := range variations{
		trees_found := check_all_lines(path, variant[0], variant[1])
		total = trees_found * total
	}
	return total
}

func main() {
    
	total := check_all_variations("day3_input.txt")
	fmt.Println(total)

}