def check_selection(numbers):
    hex_list = ["A", "B", "C", "D", "E", "F", "0", "1",
                "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper() in hex_list:  # modified the if statement
            print("Good job! The input is a hexadecimal number!")
            continue  # continue to the next iteration if it's not a hexadecimal number
        else:
            print("Not a hexadecimal number")
            return True # return back so that the user can select another number. 
        return False

def main():
    good_selection = True  # modified the initial value
    while good_selection:  # modified the loop condition
        selection = input("Provide a hexadecimal number: ")
        good_selection = check_selection(selection)

if __name__ == "__main__":
    main()
