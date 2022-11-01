import typing as tp
import math

"""

- Возможность ввода всей цепочки операций целиком и ее решение, 
если она введена корректно. Цепочка может содержать скобки (для тех, у кого получилось 
все остальное)


Для реализации тригонометрических функций можно использовать 
функции модуля math.
Продемонстрируйте работу программы. Для этого реализуйте соответствующее меню.


"""


def сс(num_1, num_2):
    b = ''
    sim = '0123456789ABCDEF'
    num_1, num_2 = int(num_1), int(num_2)
    if num_1 >= 0 and num_2 > 0:
        if 0 < num_2 <= 9:
            while num_1 > 0:
                b = str(num_1 % num_2) + b
                num_1 = num_1 // num_2
            return b
        if 10 < num_2 <= 36:
            while num_1 > 0:
                b = sim[num_1 % num_2] + b
                num_1 = num_1 // num_2
            return b
        else:
            print('')
    else:
        return f"Числa должны быть положительными"


def input_check():
    while True:
        num = input("Введите число > ")
        if num.isdigit():
            return int(num)
        else:
            n = num.split(".")
            if len(n) == 2 and n[0].isdigit() and n[1].isdigit():
                return float(num)


def match_case_calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    match command:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "/":
            if num_2 != 0:
                return num_1 + num_2
            else:
                return f"Error"
        case "*":
            return num_1 * num_2
        case "**":
            return num_1 ** num_2
        case "sin":
            return math.sin(num_1)
        case "cos":
            return math.cos(num_1)
        case "tan":
            return math.tan(num_1)
        case "^2":
            return num_1 ** 2
        case "logn":
            return math.log(num_1)
        case "log(n)":
            return math.log(num_1, num_2)
        case "log(10)":
            return math.log10(num_1)
        case "перевод":
            return сс(num_1, num_2)
        case _:
            return f"Неизвестный оператор: {command!r}."



if __name__ == "__main__":
    while True:
        COMMAND = input("Введите оперцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        NUM_1 = input_check()
        NUM_2 = input_check()
        print(match_case_calc(NUM_1, NUM_2, COMMAND))

