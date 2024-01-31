# Decimal to Binary and Binary to Decimal Converter

# Opening statement
print("Welcome to the Decimal to Binary and Binary to Decimal Converter!")

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

# Menu and program loop
def main():
    while True:
        print("\nPlease select an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            decimal = int(input("Enter a decimal number: "))
            binary = decimal_to_binary(decimal)
            print("Decimal {} to Binary: {}".format(decimal, binary))
        elif choice == '2':
            binary = int(input("Enter a binary number: "))
            decimal = binary_to_decimal(binary)
            print("Binary {} to Decimal: {}".format(binary, decimal))
        elif choice == '3':
            print("Thank you for using the Decimal to Binary and Binary to Decimal Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
