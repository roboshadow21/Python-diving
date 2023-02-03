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

# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

# fraction addition

numerator1, denominator1 = map(int, (input("Enter fraction as a/b: ").split("/")))
numerator2, denominator2 = map(int, (input("Enter fraction as c/d: ").split("/")))

if denominator1 == 0 or denominator2 == 0:
    print("Not a fraction!")

else:
    if denominator1 == denominator2:
        print(f"{numerator1 + numerator2}/{denominator1}")

    else:
        numerator_result = (numerator1 * denominator2) + (numerator2 * denominator1)
        denominator3 = denominator1 * denominator2
        common_divider = gcd(numerator_result, denominator3)
        print(f"{numerator_result // common_divider}/{denominator3 // common_divider}")

# checking

x = fraction.Fraction(numerator1, denominator1)
y = fraction.Fraction(numerator2, denominator2)
print(x + y)
