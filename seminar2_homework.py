import fraction
from math import gcd

# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

SAMPLE = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
BASE = 16

result_list = []

num = int(input("Enter decimal number: "))

# checking

print(str(hex(num))[2:])

# convert to hex format

while num != 0:
    idx = num % BASE
    result_list.append(SAMPLE[idx])
    num //= BASE

hex_num = reversed(result_list)

print("".join(hex_num))