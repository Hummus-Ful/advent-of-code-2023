#!/usr/bin/env python3

def find_digit(input):
    for char in input:      
        if char.isdigit():
            return char

total = 0
with open("Input01.txt") as input_file:
    for line in input_file:
        first = find_digit(line)
        last = find_digit(line[::-1])
        string_representation_of_sum = f"{first}{last}"
        total = total + int(string_representation_of_sum)
print(total)
