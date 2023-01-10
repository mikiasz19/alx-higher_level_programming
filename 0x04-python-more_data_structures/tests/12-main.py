#!/usr/bin/python3
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{0} = {1}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{0} = {1}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{0} = {1}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{0} = {1}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{0} = {1}".format(roman_number, roman_to_int(roman_number)))
