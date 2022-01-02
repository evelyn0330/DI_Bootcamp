import string, re

class Text:
    def __init__(self, text: str):
        self.text = text

    def check_frequency(self, word: str):
        occurences = self.text.count(word)
        return occurences

    def most_common_words(self):
        frequency = 0
        for word in self.text:
            if self.check_frequency(word) > frequency:
                frequency = self.check_frequency(word)
                return word

    def unique_words(self):
        words_list = []
        for word in self.text:
            if self.check_frequency(word) == 1:
                words_list.append(word)
            print(words_list)


class TextModification(Text):
    def no_punctuation(self):
        new_text = re.sub(r'[^\w\s]','', self.text)
        return new_text

    def no_stopwords(self):
        with open('stopwords.txt') as file:
            stopwords_list = file.read().split()
            new_list = [i for i in self.text.split() if i not in stopwords_list]
            print(' '.join(new_list))


with open('/Users/evelynpello/Desktop/DI_Bootcamp/week10/day4/Daily Challenge/the_stranger.txt') as f:
    file_text = f.read()

analysis = Text(file_text)

