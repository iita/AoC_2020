package main
import "fmt"
import "io/ioutil"
import "strings"
import "strconv"


func check_add(number1, number2 int64){
	if number1 + number2 == 2020{
		fmt.Println(number1*number2)
	}
}

func check_add_3(number1, number2, number3 int64){
	if number1 + number2 + number3 == 2020{
		fmt.Println(number1*number2*number3)
	}
}

func check_nr(name1 string) int64 {
	number, err := strconv.ParseInt(name1, 10, 64)
	if err != nil{
		
	}
	return number
}

func main() {
	content, err := ioutil.ReadFile("1974.txt")
	if err != nil {
		fmt.Println("error")
	}
	lines := strings.Split(string(content), "\r\n")
	for _, name := range lines{
		number := check_nr(name)
		if err == nil {
			for _, name2 := range lines{
				number2 := check_nr(name2)
				check_add(number, number2)
				for _, name3 := range lines{
					number3 := check_nr(name3)
					check_add_3(number, number2, number3)
				}
			}
		}
	}
}