#!/usr/bin/env python3



def find_first_and_last_numbers(line):
    numbers_as_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    index_first_num = None
    val_first_num = 0
    index_last_num = None
    val_last_num = 0
    for num in numbers_as_strings:  # check for numbers as strings
        if num in line:
            if index_first_num is None:
                index_first_num = line.find(num)
                val_first_num = numbers_as_strings.index(num)+1
                index_last_num = index_first_num
                val_last_num = val_first_num
            elif index_first_num > line.find(num):
                val_first_num = numbers_as_strings.index(num)+1
                index_first_num = line.find(num)
            if index_last_num < line.rfind(num):
                index_last_num = line.rfind(num)
                val_last_num = numbers_as_strings.index(num)+1
    for char in line:  # check for numbers as digits
        if char.isdigit():
            index_of_first_occurrance = line.find(char)
            if index_first_num is None or index_first_num > index_of_first_occurrance:
                index_first_num = index_of_first_occurrance
                val_first_num = char
            index_of_last_occurrance = line.rfind(char)
            if index_last_num is None or index_last_num < index_of_last_occurrance:
                index_last_num = index_of_last_occurrance
                val_last_num = char
    return val_first_num, val_last_num

def convert_to_int(string):
    return numbers_as_strings.index(string)


with open("Input01.txt") as input_file:
    total = 0
    for line in input_file:
        val_first_num, val_last_num = find_first_and_last_numbers(line.strip("\n"))
        string_representation_of_sum = f"{val_first_num}{val_last_num}"
        total = total + int(string_representation_of_sum)
        print(f"Line: {line.strip("\n")}, First: {val_first_num}, Last: {val_last_num}, Sum: {string_representation_of_sum}, New total: {total}")
        
    print(total)
