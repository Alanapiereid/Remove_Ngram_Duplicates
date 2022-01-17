from nltk import ngrams
from collections import Counter

def get_grams(text, n):
    text = text.lower()
    trigrams = ngrams(text.split(), n)
    collection = []

    for x in trigrams:
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

def attempt(text):
    try:
        print(get_grams(text, 4))
    except IndexError:
            pass

    try:
        print(get_grams(text, 3))
    except IndexError:
        pass

    try:
        print(get_grams(text, 2))
    except IndexError:
        pass

sentence = "The thing the thing is I hate you so much, you're amazing"

attempt(sentence)
