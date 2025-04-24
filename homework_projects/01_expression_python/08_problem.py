
SENTENCE_START : str = "I couldn't believe my eyes when I saw"
def main():
   
   adjective_word : str = input("please type an adjective word and press enter: ")
   noun_word : str = input("please type a noun word and press enter: ")
   verb_word : str = input("Please type a verb word and press enter.")

   magic_sentance =  f"{SENTENCE_START} {adjective_word} {noun_word} {verb_word}"
   print(magic_sentance)

if __name__ == '__main__':
    main()