import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input("Enter your text:\n").lower())

what_to_do = input("Enter encrypt to ENCRYPT, decrypt to DECRYPT, or exit to EXIT:\n").lower()

shift_number = int(input("Enter you shift number from 1 to 25:\n"))

end_program = False

while not end_program:
    if what_to_do == "encrypt":
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str,sentence)))
        end_program = True
    elif what_to_do == "decrypt":
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str,sentence)))
        end_program = True
