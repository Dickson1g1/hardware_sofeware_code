def check_selection(numbers): # verify if it is a hexadecimal
    hex_list = ["A", "B", "C", "D", "E", "F", "0", "1",
                "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper()  in hex_list: #check if the number is not in hex list
            print("This is a hexadecimal number")
        elif:
            print("That not a vlaid hexadecimal number")
        else:()
            return(True)

    return(True)

def main():
    good_selection = True
    while  good_selection:
        selection = input("Provide a hexadecimal number:")
        good_selection = check_selection(selection)
    print("Good job", selection, "is a hexadecimal number!!!")

if __name__ == "__main__":
    main()
