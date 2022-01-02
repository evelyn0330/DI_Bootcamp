from anagram_checker import AnagramChecker

def main():
 active = True

 while active:
    user_menu = input("Type a word you want the anagram of, or type 'quit' to exit the program: ")
    user_menu = user_menu.strip()
    if user_menu.lower() == "quit":
        print("Okay. Bye!")
        active = False
    elif len(user_menu.split()) > 1:
        print("Sorry! But only one word is accepted.")
        continue
    elif not user_menu.isalpha():
        print("Sorry! But only letters are accepted.")
        continue
    else: 
        anagram = AnagramChecker()
        if not anagram.is_valid_word(user_menu):
            print("Sorry! This is not a valid word.")
            continue
        else:
            anagrams_list = anagram.get_anagrams(user_menu)
            print(f"Your word is {user_menu}.\nThis is a valid English word.\nThe anagrams for this word are: {' '.join(anagrams_list)}")


main()