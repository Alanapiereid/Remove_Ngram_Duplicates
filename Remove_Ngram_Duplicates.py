from nltk import ngrams
from collections import Counter

class duplicate_rem:
    def __init__(self, text):
        self.text = text

    def get_grams(self, text, n):

        text = text.lower()
        n_grams = ngrams(text.split(), n)
        collection = []

        for x in n_grams:
            collection.append(' '.join(x))

        counter = Counter

        obj = counter(collection)

        drop_words = []
        for key in obj:
            if obj[key] > 1:
                drop_words.append(key)
                
        text = text.replace(drop_words[0], "")
        text = text.replace("  ", ' ' + drop_words[0] + ' ')
        return text.strip().capitalize()

    def attempt(self):
        the_list = []
        try:
            the_list.append(self.get_grams(self.text, 4))
        except IndexError:
                pass
        try:
            the_list.append(self.get_grams(self.text, 3))
        except IndexError:
            pass
        try:
            the_list.append(self.get_grams(self.text, 2))
        except IndexError:
            pass
        return the_list[0]

sentence = "The thing the thing is I love you so much, it's amazing"
sentence2 = "The thing is really the thing is really I love you so much, it's amazing"

print(duplicate_rem(sentence).attempt())
# The thing is i love you so much, it's amazing
print(duplicate_rem(sentence2).attempt())
# The thing is really i love you so much, it's amazing

