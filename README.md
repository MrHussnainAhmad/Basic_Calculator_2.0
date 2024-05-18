# Basic_Calculator_2.0
Description:

The provided Python script implements a command-line calculator that allows users to perform various arithmetic operations on two numbers. It prompts the user to select between integer and float conversion modes and then proceeds to accept two numbers and an arithmetic operation choice from the user. The script then calculates and displays the result based on the user's input.
Features:

    Conversion Type Selection:
        The user is prompted to choose between integer (I) and float (F) conversion modes.
        Based on the selected mode, the script accepts input numbers as integers or floats.

    Number Input:
        After selecting the conversion mode, the user is asked to input two numbers.
        The input numbers are validated based on the selected conversion mode (integer or float).

    Arithmetic Operations:
        The user is presented with a list of arithmetic operations to choose from:
            Addition (+)
            Subtraction (-)
            Multiplication (*)
            Division (/)
            Modulus (%)
            Exponential (pow)
            Square (Square)
            Cube (Cube)
            Square Root (Sq root)
        Based on the user's selection, the corresponding arithmetic operation is performed.

    Error Handling:
        The script handles various error conditions, such as invalid conversion mode inputs, division by zero, and invalid arithmetic operation choices.
        If an error occurs, an appropriate error message is displayed, and the user is given the option to restart the calculation process.

Detailed Code Explanation:

    Function Definition:
        The entire calculator functionality is encapsulated within the new_func() function.

    Conversion Mode Selection:
        The script prompts the user to select the conversion mode (I for integer, F for float).
        The user's input is converted to lowercase for case-insensitive comparison.

    Input Validation and Arithmetic Operation:
        Depending on the selected conversion mode, the script accepts input numbers as integers or floats.
        After accepting the numbers, the script presents the user with a list of arithmetic operations to choose from.
        The script performs the selected arithmetic operation on the input numbers and displays the result.

    Error Handling and Restart Option:
        If the user enters an invalid conversion mode or arithmetic operation choice, appropriate error messages are displayed.
        In case of division by zero or other errors, the script notifies the user and offers the option to restart the calculation process.

Summary:

This script provides a simple and interactive command-line calculator that supports both integer and float calculations. Users can perform various arithmetic operations and receive accurate results based on their input. The script ensures error-free operation by handling invalid inputs and offering the option to restart the calculation process if needed.
