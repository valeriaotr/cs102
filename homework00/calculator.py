""" important modules """
import math
import typing as tp

""" Возможность ввода всей цепочки операций целиком и ее решение, если она введена корректно.
Цепочка может содержать скобки (для тех, у кого получилось все остальное)
Для реализации тригонометрических функций можно использовать
функции модуля math. Продемонстрируйте работу программы.
Для этого реализуйте соответствующее меню."""


def common_num(num_1, num_2):
<<<<<<< HEAD
    """function for transfer"""
=======
    """function for the first check"""
>>>>>>> 834686fb6204ae3ad82de478f7480938a2ef3f34
    b_1 = ""
    sim = "0123456789ABCDEF"
    num_1, num_2 = int(num_1), int(num_2)
    if num_1 >= 0 and num_2 > 0:
        if 0 < num_2 <= 9:
            while num_1 > 0:
                b_1 = str(num_1 % num_2) + b_1
                num_1 = num_1 // num_2
            return b_1
<<<<<<< HEAD
        else:
            return "такая система счисления недоступна"
=======
        if 10 < num_2 <= 36:
            while num_1 > 0:
                b_1 = sim[num_1 % num_2] + b_1
                num_1 = num_1 // num_2
            return b_1
>>>>>>> 834686fb6204ae3ad82de478f7480938a2ef3f34
        print("")
    return "Числa должны быть положительными"


def input_check():
    """function for input check"""
    while True:
        num = input("Введите число >")
        if num.isdigit():
<<<<<<< HEAD
            return float(num)
        else:
            return "Ошибка: Вы ввели не число"


def match_case_calc_1(num_1: float, command: str) -> tp.Union[float, str]:
    """function for math options"""
    match command:
        case "sin":
            return math.sin(num_1)
        case "cos":
            return math.cos(num_1)
        case "tan":
            return math.tan(num_1)
        case "^2":
            return num_1**2
        case "ln":
            if num_1 <= 0:
                return "невозможно по области определения"
            return math.log(num_1)
        case "lg":
            if num_1 <= 0:
                return "невозможно по области определения"
            return math.log10(num_1)
        case _:
            return f"Неизвестный оператор: {command!r}."


def match_case_calc_2(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:  # type: ignore
    match command:
=======
            return int(num)
        else:
            n_1 = num.split(".")
            if len(n_1) == 2 and n_1[0].isdigit() and n_1[1].isdigit():
                return float(num)


def match_case_calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    """function for math options"""
    match command:
>>>>>>> 834686fb6204ae3ad82de478f7480938a2ef3f34
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "/":
            if num_2 != 0:
<<<<<<< HEAD
                return num_1 / num_2
=======
                return num_1 + num_2
>>>>>>> 834686fb6204ae3ad82de478f7480938a2ef3f34
            return f"Error"
        case "*":
            return num_1 * num_2
        case "**":
            return num_1**num_2
<<<<<<< HEAD
        case "перевод":
            return common_num(num_1, num_2)
=======
        case "sin":
            return math.sin(num_1)
        case "cos":
            return math.cos(num_1)
        case "tan":
            return math.tan(num_1)
        case "^2":
            return num_1**2
        case "logn":
            return math.log(num_1)
        case "log(n)":
            return math.log(num_1, num_2)
        case "log(10)":
            return math.log10(num_1)
        case "перевод":
            return common_num(num_1, num_2)
        case _:
            return f"Неизвестный оператор: {command!r}."
>>>>>>> 834686fb6204ae3ad82de478f7480938a2ef3f34


if __name__ == "__main__":
    while True:
<<<<<<< HEAD
        try:
            COMMAND = input("Введите операцию > ")
            if COMMAND in ("+", "-", "/", "*", "**", "перевод"):
                NUM_1 = float(input("Первое число > "))
                NUM_2 = float(input("Второе число > "))
                print(match_case_calc_2(NUM_1, NUM_2, COMMAND))
            elif COMMAND in ("^2", "cos", "sin", "tan", "ln", "lg"):
                NUM_1 = float(input("Введите число > "))
                print(match_case_calc_1(NUM_1, COMMAND))
            else:
                print("Такой операции не существует")
        except ValueError:
            print("Ошибка: вы ввели не число")
            pass
=======
        COMMAND = input("Введите оперцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        NUM_1 = input_check()
        NUM_2 = input_check()
        print(match_case_calc(NUM_1, NUM_2, COMMAND))
>>>>>>> 834686fb6204ae3ad82de478f7480938a2ef3f34
