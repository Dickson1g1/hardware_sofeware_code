# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

# Function to convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        decimal += (binary % 10) * (2 ** power)
        binary = binary // 10
        power += 1
    return decimal

# Function to convert hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal)[2:]
    return hexadecimal

# Function to convert hexadecimal to binary
def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = decimal_to_binary(decimal)
    return binary

# Function to convert binary to hexadecimal
def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(int(binary))
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

# Function to convert octal to decimal
def octal_to_decimal(octal):
    decimal = int(octal, 8)
    return decimal

# Function to convert decimal to octal
def decimal_to_octal(decimal):
    octal = oct(decimal)[2:]
    return octal

# Menu and program loop
def main():
    print("Hello!")
    print("Welcome to the Number Conversion Program!") # Opening statement
    while True:
        print("\nPlease select an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Convert Hexadecimal to Decimal")
        print("4. Convert Decimal to Hexadecimal")
        print("5. Convert Hexadecimal to Binary")
        print("6. Convert Binary to Hexadecimal")
        print("7. Convert Octal to Decimal")
        print("8. Convert Decimal to Octal")
        print("9. Quit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            try:
                decimal = int(input("Enter a decimal number: "))
                binary = decimal_to_binary(decimal)
                print("Decimal {} to Binary: {}".format(decimal, binary))
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")
        elif choice == '2':
            try:
                binary = input("Enter a binary number: ")
                decimal = binary_to_decimal(int(binary))
                print("Binary {} to Decimal: {}".format(binary, decimal))
            except ValueError:
                print("Invalid input! Please enter a valid binary number.")
        elif choice == '3':
            try:
                hexadecimal = input("Enter a hexadecimal number: ")
                decimal = hexadecimal_to_decimal(hexadecimal)
                print("Hexadecimal {} to Decimal: {}".format(hexadecimal, decimal))
            except ValueError:
                print("Invalid input! Please enter a valid hexadecimal number.")
        elif choice == '4':
            try:
                decimal = int(input("Enter a decimal number: "))
                hexadecimal = decimal_to_hexadecimal(decimal)
                print("Decimal {} to Hexadecimal: {}".format(decimal, hexadecimal))
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")
        elif choice == '5':
            try:
                hexadecimal = input("Enter a hexadecimal number: ")
                binary = hexadecimal_to_binary(hexadecimal)
                print("Hexadecimal {} to Binary: {}".format(hexadecimal, binary))
            except ValueError:
                print("Invalid input! Please enter a valid hexadecimal number.")
        elif choice == '6':
            try:
                binary = input("Enter a binary number: ")
                decimal = binary_to_decimal(int(binary))
                print("Binary {} to Decimal: {}".format(binary, decimal))
            except ValueError:
                print("Invalid input! Please enter a valid binary number.") # i have to compelet my code.
                #from here. 
if __name__ == '__main__':
    main()
