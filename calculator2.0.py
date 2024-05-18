def new_func():
    print()
    print("Welcome!")
    print("May I know whether you want an integer conversion or float?")
    conversion = input("Enter I or F, respectively: ").lower()

    if conversion == "i":
        print()
        print("Thanks for cooperating, you may start conversion!")
        input1 = int(input("Enter the First Number: "))
        input2 = int(input("Enter the Second Number: "))
    elif conversion == "f":
        print()
        print("Thanks for cooperating, you may start conversion!")
        input1 = float(input("Enter the First Number: "))
        input2 = float(input("Enter the Second Number: "))
    else:
        print("Invalid input for conversion type!")
        print("Want to restart again?")
        rA = input("Enter Y/n: ").lower()
        if rA == "y":
            new_func()
            print()
        else:
            exit()
        return

    print()
    print("Select one of the following operations:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. %")
    print("6. pow")
    print("7. Square")
    print("8. Cube")
    print("9. Sq root")
    user = input("Enter your choice: ")

    if user == "1":
        result = input1 + input2
    elif user == "2":
        result = input1 - input2
    elif user == "3":
        result = input1 * input2
    elif user == "4":
        if input2 == 0:
            print("Error! Division by zero is not allowed.")
            return
        result = input1 / input2
    elif user == "5":
        result = input1 % input2
    elif user == "6":
        result = input1 ** input2
    elif user == "7":
        result = input1 ** 2
    elif user == "8":
        result = input1 ** 3
    elif user == "9":
        result = input1 ** 0.5
    else:
        print("Invalid option!")
        return

    print()
    print("Result:", result)

new_func()

