def decimal_to_binary(number):
    try:
        result = ""
        number = int(number)
        while number > 0:
            remainder = number % 2
            number = number // 2
            result = str(remainder) + result
        return result
    except ValueError:
        print("Invalid input! Please enter a valid decimal number.")

def main():
    num = input("Enter Decimal Number:")
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

if __name__ == "__main__":
    main()
