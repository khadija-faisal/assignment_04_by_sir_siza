





def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("She placed the mysterious " + word + " on the table, whispering about its strange origin.")
    elif part_of_speech == 1:
        # verb
        print("Whenever I hear that song, I just want to " + word + " through the empty streets!")
    elif part_of_speech == 2:
        # adjective
        print("The mountain air was crisp and " + word + " wrapping everything in quiet stillness.")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

# There is no need to edit code beyond this point

def main():
    word :  str = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
