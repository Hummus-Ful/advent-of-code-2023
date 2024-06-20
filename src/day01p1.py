#!/usr/bin/env python3

def find_digit(input):
    for char in input:      
        if char.isdigit():
            return char

def main(file):
    total = 0
    try:
        with open(file) as input_file:
            for line in input_file:
                first = find_digit(line)
                last = find_digit(line[::-1])
                string_representation_of_sum = f"{first}{last}"
                total = total + int(string_representation_of_sum)
        print(total)
        return total
    except FileNotFoundError:
        print("Please cd into src directory to run the script")

if __name__ == '__main__':
    main("day01_input.txt")