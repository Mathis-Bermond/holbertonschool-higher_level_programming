#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = number % 10 if number >= 0 else (abs(number) % 10)
str1 = "Last digit of"
str2 = "is"
str3 = "and is greater than 5"
str4 = "and is 0"
str5 = "and is less than 6 and not 0"
if last_d > 5:
    print(f"{str1} {number} {str2} {last_d} {str3}")
elif last_d == 0:
    print(f"{str1} {number} {str2} {last_d} {str4}")
elif last_d < 6 and last_d != 0:
    print(f"{str1} {number} {str2} {last_d} {str5}")
