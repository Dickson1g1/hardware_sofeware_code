def get_smallest(smallest, value):
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    return smallest

def main():
    smallest = None
    while True:
        num = int(input("Enter a number: ").lower())    
        if num == "done":
            break
        smallest = get_smallest(smallest, num)
        print("Smllest number is:", smallest)

if __name__ == "__main__":
    main()
