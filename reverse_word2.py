def intro_msg():
    print("I can reverse a string")
    print("If you give me 'apple', I will return 'elppa'")
    print("I can even reverse an entire sentence")
    print("Or type done to quit")
    return input("Type something and see: ")

def reverse_word(characters):
    reverse_string = ''
    for character in characters:
        reverse_string = character + reverse_string
    return reverse_string

def main():
    while True:
        word = intro_msg()
        if word.lower() in ['quit', 'done']:
            break
        reversed_word = reverse_word(word)
        print('Below is your string in reverse:\n{}'.format(reversed_word))
        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()
