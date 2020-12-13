package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "regexp"
    "strings"
)




func main() {
    m := make(map[string]string)
    m["byr"] = ":(19[2-9][0-9]|200[0-2])\\b"
    m["eyr"] = ":(202[0-9]|2030)\\b"
    m["hgt"] = ":((1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in))\\b"
    m["hcl"] = ":#[0-9a-f]{6}\\b"
    m["ecl"] = ":(amb|blu|brn|gry|grn|hzl|oth)\\b"
    m["pid"] = ":[0-9]{9}\\b"
    m["iyr"] = ":(201[0-9]|2020)\\b"
    
    valid_passports := 0

    content, err := ioutil.ReadFile("day4_input.txt")
    if err != nil {
        log.Fatal(err)
    }
    r, _ := regexp.Compile("\\b([a-z]+):\\b")
    split_content := strings.Split(string(content), "\n\r")
    for _, group := range(split_content) {
        all_matches := r.FindAllStringSubmatch(group,-1)
        fmt.Println(all_matches)
        

        n_found := 0
        for key, element := range m{
            key_string := "\\b" + key + element
            r_s, _ := regexp.Compile(key_string)
            fmt.Println(r_s)
            if r_s.MatchString(group){
                n_found++
            }

            
        }
    fmt.Println(valid_passports)

    }
    
}
