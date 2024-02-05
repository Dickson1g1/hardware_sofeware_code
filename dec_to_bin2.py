def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:   # keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result   # place string in reverse order
    return result

def main():
    while True:
        num = input("Enter Decimal Number: ")
        if num.isdigit():
            print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))
            break
        else:
            print("Invalid input! Please enter a valid decimal number.")

if __name__ == "__main__":
    main()
