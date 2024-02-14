
number1 = int(input())
action = input()
number2 = int(input())


if action == '+':
    print("Результат действия:", number1 + number2)

elif action == '-':
    print("Результат действия:", number1 - number2)

elif action == '*':
    print("Результат действия:", number1 * number2)

elif action == '/':
    if number2 != 0:
        print("Результат действия:", number1 / number2)
    else:
        print("Результат действия:", "Числа на ноль не делятся")
