string = (input("Give me a word! "))
if len(string) < 10:
    print("Word is not long enough!")
elif len(string) > 10:
    print("Word is too long!")
else:
    print("This is the first letter of your word:",string[0],"and this is the last letter of your word:",string[-1])

i = 0
while i < len(string):
    i += 1
    print(string[0:i])

import random
jumbled = list(string)
random.shuffle(jumbled)
print(''.join(jumbled))