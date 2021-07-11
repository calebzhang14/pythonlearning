def calculator():
    print("Type one number. Then press enter or return.")
    number1 = float(input())

    print("Put operation sign: one of the following: + - * /")
    op = input()

    if (op != '+' and op != '-' and op != '*' and op != '/'):
        print("That is invalid")
        return

    print("Type another number. Then press enter or return.")
    number2 = float(input())

    if op == '+':
        print("The answer is:" + str(number1 + number2))
    elif op == '-':
        print("The answer is:" + str(number1 - number2))
    elif op == '*':
        print("The answer is:" + str(number1 * number2))
    elif op == '/':
        print("The answer is:" + str(number1 / number2))

for i in range(1,101):
    try:
        calculator()
    except Exception as e:
        print('Failed, because of this error: '+ str(e))