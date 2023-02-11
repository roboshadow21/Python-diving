# Напишите функцию для транспонирования матрицы

MATRIX_LENGTH = 3
MATRIX_WIDTH = 3


def create_matrix(num1: int, num2: int) -> list[[int]]:
    matrix = [[i + 1 for i in range(num1)] for _ in range(num2)]
    return matrix


matr = create_matrix(MATRIX_LENGTH, MATRIX_WIDTH)

for i in matr:
    print(*i)


def transposed_matrix(matrix: list[[int]]) -> list[[int]]:
    res_matrix = list(zip(*matrix))
    return res_matrix


print()

transposed = transposed_matrix(matr)

for i in transposed:
    print(*i)


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def my_func(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        try:
            temp = hash(value)
            my_dict[temp] = key
        except TypeError:
            key_unhashable = str(value)
            my_dict[key_unhashable] = key

    return my_dict


print(my_func(a=2, b=3, c=[1, 2, 3]))


# Напишите программу банкомат


def get_cash(balance: int):
    cash = int(input("Enter summa multiply of 50: "))
    if balance == 0:
        print("Not enough cash!")
    elif cash % 50 != 0:
        print("Summa not multiply of 50! Try again")
    else:
        percent = float(1.5) * cash / 100
        if percent < 30:
            result = (balance - 30) - cash
            return result
        elif percent > 600:
            result = (balance - 600) - cash
            return result
        else:
            result = (balance - percent) - cash

            return result


def deposit_cash(balance: int):
    cash = int(input("Enter summa multiply of 50: "))
    if cash % 50 != 0:
        print("Summa not multiply of 50! Try again")
    elif balance > 5_000_000:
        res = (balance * 10) / 100
        balance -= res
    else:
        balance = cash
        return balance


def atm_machine():
    balance = 0
    result = 0
    count = 0
    operation_list = []

    while True:

        choice = int(input("Select an action:\n1 - withdraw cash\n2 - deposit cash\n3 - exit\n: "))

        if count == 3:
            balance += (3 * balance) / 100

        if choice == 1 and balance < choice:
            print("Not enough cash!")

        elif choice == 1 and balance >= choice:
            result = get_cash(balance)
            balance -= result
            count += 1

        elif choice == 2:
            result = deposit_cash(balance)
            balance += result
            count += 1

        else:
            exit()

        operation_list.append(result)
        print(f"Your balance = {balance}")


atm_machine()