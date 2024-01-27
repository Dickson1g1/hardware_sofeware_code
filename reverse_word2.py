def intro_msg():
    print("I can reverse a string")
    print("If you give me 'apple', I will return 'elppa'")
    print("I can even reverse an entire sentence")
    print("Or type done to quit") # added to make sure the user knows what the code does.
    return input("Type something and see: ")

def reverse_word(characters):
    reverse_string = ''
    for character in characters:
        reverse_string = character + reverse_string
    return reverse_string 

def main():
    while True:
        word = intro_msg()
        if word.lower() in ['done']: # added if to make sure if the user want to break out of the loop.
            break
        reversed_word = reverse_word(word)
        print('Below is your string in reverse:\n{}'.format(reversed_word))
        print("Good job!!, Let's try another one.")
        print() # Add a blank print line for a space between

if __name__ == "__main__":
    main()
