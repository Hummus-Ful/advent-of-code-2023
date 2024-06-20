#!/usr/bin/env python3

import day01p1, day01p2
import tempfile

def test_day01p1_with_example_input():
    tf = tempfile.TemporaryFile("w")
    lines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    for line in lines:
        tf.write(line + "\n")
    tf.seek(0)
    result = day01p1.main(tf.name)
    assert result == 142

def test_day01p2_with_example_input():
    tf = tempfile.TemporaryFile("w")
    lines = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
    for line in lines:
        tf.write(line + "\n")
    tf.seek(0)
    result = day01p2.main(tf.name)
    assert result == 281