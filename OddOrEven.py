def check_if_odd(n):
    isOdd = True
    if n%2 == 0:
        isOdd = False
    
    if isOdd:
        print("I am odd!!!")
    else:
        print("I am even!!!")

input_str = input("Enter number: ")
num = int(input_str)
check_if_odd(num)