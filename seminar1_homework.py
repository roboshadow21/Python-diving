# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним

a = 2
b = 3
c = 3

if a + b < c or a + c < b or b + c < a:
    print("Not a triangle!")

else:
    if a != b and a != c and b != c:
        print("The versatile triangle")
    elif a == b and a == c and b == c:
        print("The equilateral triangle")
    else:
        print("The isosceles triangle")


# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LIMIT = 2

while True:
    num = int(input("Enter any number between 2 and 100 000: "))

    if num < 0 or num > 100000:
        print(f"{num} - wrong number!")
        break

    elif num == 0 or num == 1:
        print(f"{num} is not the composite or prime number")

    else:
        for i in range(LIMIT, num):
            if num % i == 0:
                print(f"{num} is the composite number")
                break
        else:
            print(f"{num} is the prime number")