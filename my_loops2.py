def while_counter(num):
    num = 1
    while num < 11:
        print("While count:{}".format(num))
        num += 1

def for_counter(num):
    for count in range(11):
        print("For count:{}".format(count))

def main():
    counter = 10
    while_counter(counter)
    for_counter(counter)

if __name__ == "__main__":
    main()
